import pandas as pd
import os
from .session import TDASession
from .exceptions import handle_error_response, TDAAPIError
from .urls import (
    # --ORDERS--
    CANCEL_ORDER,
    # GET_ORDER,
    # GET_ORDERS_BY_PATH,
    GET_ORDER_BY_QUERY,
    PLACE_ORDER,
    REPLACE_ORDER,
    STATUS_VALUES,
    # --SAVED ORDERS--
    CREATE_SAVED_ORDER,
    DELETE_SAVED_ORDER,
    GET_SAVED_ORDER,
    GET_SAVED_ORDER_BY_PATH,
    REPLACE_SAVED_ORDER,
    # --ACCOUNTS--
    GET_ACCOUNT,
    GET_ACCOUNTS,
    # --AUTHENTICATION--
    # ACCESS_TOKEN,
    # --INSTRUMENTS--
    SEARCH_INSTRUMENTS,
    SEARCH_INSTRUMENT_PROJECTION,
    GET_INSTRUMENT,
    # --MARKET HOURS--
    GET_HOURS_FOR_MULTIPLE_MARKETS,
    MARKETS_VALUES,
    GET_HOURS_FOR_SINGLE_MARKET,
    # --MOVERS--
    MOVERS,
    DIRECTION_VALUES,
    CHANGE_VALUES,
    # --OPTION CHAINS--
    GET_OPTION_CHAIN,
    CONTRACT_TYPE_VALUES,
    STRATEGY_VALUES,
    RANGE_VALUES,
    OPTION_TYPE_VALUES,
    OPTION_EXPMONTH_VALUES,
    # --PRICE HISTORY--
    GET_PRICE_HISTORY,
    PERIOD_TYPE_VALUES,
    FREQUENCY_TYPE_VALUES,
    # --QUOTES--
    # GET_QUOTE,
    GET_QUOTES,
    # --TRANSACTION HISTORY--
    # GET_TRANSACTION,
    # GET_TRANSACTIONS,
    GET_TRANSCATION_TYPE_VALUES,
    # --User Info/Prefs--
    GET_PREFERENCES,
    # GET_STREAMER_SUBSCRIPTION_KEYS,
    # GET_USER_PRINCIPALS,
    # USER_PRINCIPALS_FIELDS_VALUES,
    UPDATE_PREFERENCES,
    # --WATCHLIST--
    CREATE_WATCHLIST,
    DELETE_WATCHLIST,
    GET_WATCHLIST,
    # GET_WATCHLISTS_MULTIPLE_ACCOUNTS,
    GET_WATCHLISTS,
    GET_WATCHLISTS_MULTIPLE_ACCOUNTS,
    REPLACE_WATCHLIST,
    UPDATE_WATCHLIST,
)


def response_is_valid(resp):
    return resp.status_code in (200, 201, 204)


class TDClient(object):
    def __init__(self, client_id=None, refresh_token=None, account_ids=None):
        self._clientId = client_id or os.environ["TDAMERITRADE_CLIENT_ID"]
        self._refreshToken = refresh_token or os.environ["TDAMERITRADE_REFRESH_TOKEN"]
        self.accountIds = account_ids or []
        self.session = TDASession(self._refreshToken, self._clientId)

    def _request(self, url, method="GET", params=None, *args, **kwargs):
        resp = self.session.request(method, url, params=params, *args, **kwargs)
        if not response_is_valid(resp):
            handle_error_response(resp)
        return resp

    def accounts(self, positions=False, orders=False):
        """get user accounts. caches account ids in accountIds if not provided during initialization

        Args:
            positions (bool): include position information
            orders (bool): include order information
        """
        ret = {}

        if positions or orders:
            params = {"fields": []}

            if positions:
                params["fields"].append("positions")
            if orders:
                params["fields"].append("orders")
            params["fields"] = ",".join(params["fields"])
        else:
            params = {}

        if self.accountIds:
            for acc in self.accountIds:
                resp = self._request(GET_ACCOUNT.format(accountId=acc), params=params)
                ret[acc] = resp.json()
        else:
            resp = self._request(GET_ACCOUNTS, params=params)
            for account in resp.json():
                ret[account["securitiesAccount"]["accountId"]] = account
            self.accountIds = [int(accountId) for accountId in ret]
        return ret

    def accountsDF(self):
        """get accounts as dataframe"""
        data = self.accounts()
        account_dataframes = []
        for accountId, value in data.items():
            account_dataframes.append(pd.io.json.json_normalize(value))
            account_dataframes[-1].columns = [
                c.replace("securitiesAccount.", "")
                for c in account_dataframes[-1].columns
            ]
        return pd.concat(account_dataframes)

    def transactions(
        self, accountId=None, type=None, symbol=None, startDate=None, endDate=None
    ):
        """get transactions by account

        Args:
            accountId (int): account id (defaults to client's ids)
            type (str): transaction type, in ('ALL', 'TRADE', 'BUY_ONLY', 'SELL_ONLY', 'CASH_IN_OR_CASH_OUT', 'CHECKING', 'DIVIDEND', 'INTEREST', 'OTHER', 'ADVISOR_FEES')
            symbol (str): transactions for given symbol
            start_date (str): start date as string yyyy-MM-dd
            end_date (str): end date as string yyyy-MM-dd
        """
        if accountId:
            accounts = [accountId]
        else:
            accounts = self.accountIds

        if type not in GET_TRANSCATION_TYPE_VALUES:
            raise TDAAPIError(
                "Transaction type must be in {}".format(GET_TRANSCATION_TYPE_VALUES)
            )

        ret = {}
        for account in accounts:
            transactions = GET_ACCOUNT.format(accountId=account) + "/transactions"
            ret[account] = self._request(
                transactions,
                params={
                    "type": type,
                    "symbol": symbol,
                    "startDate": startDate,
                    "endDate": endDate,
                },
            ).json()
        return ret

    def transactionsDF(
        self, accountId=None, type=None, symbol=None, startDate=None, endDate=None
    ):
        """get transaction information as Dataframe"""
        return pd.json_normalize(
            self.transactions(
                accountId=accountId,
                type=type,
                symbol=symbol,
                startDate=startDate,
                endDate=endDate,
            )
        )

    def search(self, symbol, projection="symbol-search"):
        """Search for a symbol

        Args:
            symbol (sring): string to search for
            projection (string): projection to use, in ('symbol-search', 'symbol-regex', 'desc-search', 'desc-regex', 'fundamental')
        """
        if projection not in SEARCH_INSTRUMENT_PROJECTION:
            raise TDAAPIError(
                "Projection must be in {}".format(SEARCH_INSTRUMENT_PROJECTION)
            )

        return self._request(
            SEARCH_INSTRUMENTS, params={"symbol": symbol, "projection": projection}
        ).json()

    def searchDF(self, symbol, projection="symbol-search"):
        """search for symbol as a dataframe"""
        ret = []
        dat = self.search(symbol, projection)
        for symbol in dat:
            ret.append(dat[symbol])

        return pd.DataFrame(ret)

    def fundamentalSearch(self, symbol):
        """helper to search for a symbol using fundamental projection"""
        return self.search(symbol, "fundamental")

    def fundamentalSearchDF(self, symbol):
        """helper to search for a symbol using fundamental projection and return DF"""
        return self.searchDF(symbol, "fundamental")

    def instrument(self, cusip):
        """get instrument info from cusip

        Args:
            cusip (str): the cusip to use, can find it by looking up in search
        """
        return self._request(GET_INSTRUMENT.format(cusip=cusip)).json()

    def instrumentDF(self, cusip):
        """get instrument info from cusip as dataframe"""
        return pd.DataFrame(self.instrument(cusip))

    def quote(self, symbol):
        """get quote for symbol

        Args:
            symbol (str): symbol to get quote for
        """
        if not isinstance(symbol, list):
            symbol = [symbol]

        return self._request(
            GET_QUOTES, params={"symbol": [s.upper() for s in symbol]}
        ).json()

    def quoteDF(self, symbol):
        """get quote, format as dataframe"""
        x = self.quote(symbol)

        return pd.DataFrame(x).T.reset_index(drop=True)

    def history(
        self,
        symbol,
        periodType=None,
        period=None,
        frequencyType=None,
        frequency=None,
        endDate=None,
        startDate=None,
        needExtendedHoursData=True,
    ):
        """get price history

        Args:
            symbol (str): symbol to get price history for
            periodType (str): period type to request
            period (int): period to use
            frequencyType (str): frequency type to use
            frequency (int): frequency to use
            endDate (int): End date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided. Default is previous trading day.
            startDate (int): Start date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided.
            needExtendedHoursData (bool): true to return extended hours data, false for regular market hours only. Default is true
        """
        params = {}
        if periodType or period:
            if periodType not in PERIOD_TYPE_VALUES:
                raise TDAAPIError(
                    "Period type must be in {}".format(PERIOD_TYPE_VALUES)
                )
            params["period"] = period
            params["periodType"] = periodType
        if frequencyType or frequency:
            if frequencyType not in FREQUENCY_TYPE_VALUES:
                raise TDAAPIError(
                    "Frequency type must be in {}".format(FREQUENCY_TYPE_VALUES)
                )
            params["frequency"] = frequency
            params["frequencyType"] = frequencyType

        if startDate:
            params["startDate"] = startDate

        if endDate:
            params["endDate"] = endDate

        params["needExtendedHoursData"] = needExtendedHoursData

        return self._request(
            GET_PRICE_HISTORY.format(symbol=symbol), params=params
        ).json()

    def historyDF(self, symbol, **kwargs):
        """get history as dataframe"""
        x = self.history(symbol, **kwargs)
        df = pd.DataFrame(x["candles"])
        df["datetime"] = pd.to_datetime(df["datetime"], unit="ms")

        return df

    def options(
        self,
        symbol,
        contractType="ALL",
        strikeCount=-1,
        includeQuotes=False,
        strategy="SINGLE",
        interval=None,
        strike=None,
        range="ALL",
        fromDate=None,
        toDate=None,
        volatility=None,
        underlyingPrice=None,
        interestRate=None,
        daysToExpiration=None,
        expMonth="ALL",
        optionType="ALL",
    ):
        """request option chain information

        Args:
            symbol (str): Enter one symbol
            contractType (str): Type of contracts to return in the chain. Can be CALL, PUT, or ALL. Default is ALL.
            strikeCount (int): The number of strikes to return above and below the at-the-money price.
            includeQuotes (bool): Include quotes for options in the option chain. Can be TRUE or FALSE. Default is FALSE.
            strategy (str): Passing a value returns a Strategy Chain. Possible values are SINGLE, ANALYTICAL (allows use of the volatility, underlyingPrice, interestRate, and daysToExpiration params to calculate theoretical values), COVERED, VERTICAL, CALENDAR, STRANGLE, STRADDLE, BUTTERFLY, CONDOR, DIAGONAL, COLLAR, or ROLL. Default is SINGLE.
            interval (int): Strike interval for spread strategy chains (see strategy param).
            strike (float): Provide a strike price to return options only at that strike price.
            range (str): Returns options for the given range. Possible values are:
                            ITM: In-the-money
                            NTM: Near-the-money
                            OTM: Out-of-the-money
                            SAK: Strikes Above Market
                            SBK: Strikes Below Market
                            SNK: Strikes Near Market
                            ALL: All Strikes
                            Default is ALL.
            fromDate (str): Only return expirations after this date. For strategies, expiration refers to the nearest term expiration in the strategy. Valid ISO-8601 formats are: yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.
            toDate (str): Only return expirations before this date. For strategies, expiration refers to the nearest term expiration in the strategy. Valid ISO-8601 formats are: yyyy-MM-dd and yyyy-MM-dd'T'HH:mm:ssz.
            volatility (float): Volatility to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
            underlyingPrice (float): Underlying price to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
            interestRate (float): Interest rate to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
            daysToExpiration (int): Days to expiration to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).
            expMonth (str): Return only options expiring in the specified month. Month is given in the three character format.
                                Example: JAN
                                Default is ALL.
            optionType (str): Type of contracts to return. Possible values are:
                                S: Standard contracts
                                NS: Non-standard contracts
                                ALL: All contracts
                                Default is ALL.
        """
        params = {"symbol": symbol}

        if contractType not in CONTRACT_TYPE_VALUES:
            raise TDAAPIError(
                "Contract type must be in {}".format(CONTRACT_TYPE_VALUES)
            )
        params["contractType"] = contractType

        if strikeCount:
            params["strikeCount"] = strikeCount

        params["includeQuotes"] = includeQuotes

        if strategy not in STRATEGY_VALUES:
            raise TDAAPIError("Strategy must be in {}".format(STRATEGY_VALUES))

        params["strategy"] = strategy

        if interval:
            params["interval"] = interval

        if strike:
            params["strike"] = strike

        if range not in RANGE_VALUES:
            raise TDAAPIError("Range must be in {}".format(RANGE_VALUES))

        params["range"] = range

        if fromDate:
            params["fromDate"] = fromDate

        if toDate:
            params["toDate"] = toDate

        if strategy == "ANALYTICAL":
            if volatility:
                params["volatility"] = volatility
            if underlyingPrice:
                params["underlyingPrice"] = underlyingPrice
            if interestRate:
                params["interestRate"] = interestRate
            if daysToExpiration:
                params["daysToExpiration"] = daysToExpiration

        if expMonth not in OPTION_EXPMONTH_VALUES:
            raise TDAAPIError(
                "Expiration month must be in {}".format(OPTION_EXPMONTH_VALUES)
            )
        params["expMonth"] = expMonth

        if optionType not in OPTION_TYPE_VALUES:
            raise TDAAPIError("Option type must be in {}".format(OPTION_TYPE_VALUES))

        return self._request(GET_OPTION_CHAIN, params=params).json()

    def optionsDF(
        self,
        symbol,
        contractType="ALL",
        strikeCount=-1,
        includeQuotes=False,
        strategy="SINGLE",
        interval=None,
        strike=None,
        range="ALL",
        fromDate=None,
        toDate=None,
        volatility=None,
        underlyingPrice=None,
        interestRate=None,
        daysToExpiration=None,
        expMonth="ALL",
        optionType="ALL",
    ):
        """return options chain as dataframe"""
        ret = []
        dat = self.options(
            symbol=symbol,
            contractType=contractType,
            strikeCount=strikeCount,
            includeQuotes=includeQuotes,
            strategy=strategy,
            interval=interval,
            strike=strike,
            range=range,
            fromDate=fromDate,
            toDate=toDate,
            volatility=volatility,
            underlyingPrice=underlyingPrice,
            interestRate=interestRate,
            daysToExpiration=daysToExpiration,
            expMonth=expMonth,
            optionType=optionType,
        )
        for date in dat["callExpDateMap"]:
            for strike in dat["callExpDateMap"][date]:
                ret.extend(dat["callExpDateMap"][date][strike])
        for date in dat["putExpDateMap"]:
            for strike in dat["putExpDateMap"][date]:
                ret.extend(dat["putExpDateMap"][date][strike])

        df = pd.DataFrame(ret)
        for col in (
            "tradeTimeInLong",
            "quoteTimeInLong",
            "expirationDate",
            "lastTradingDay",
        ):
            df[col] = pd.to_datetime(df[col], unit="ms")

        return df

    def movers(self, index, direction="up", change="percent"):
        """request market movers

        Args:
            index (str): index to look for movers in
            direction (str): up or down
            change (str): percent or value
        """
        params = {}
        if direction not in DIRECTION_VALUES:
            raise TDAAPIError("Direction must be in {}".format(DIRECTION_VALUES))
        params["direction"] = direction

        if change not in CHANGE_VALUES:
            raise TDAAPIError("Change mus be in {}".format(CHANGE_VALUES))
        params["change"] = change

        return self._request(MOVERS.format(index=index), params=params).json()

    def orders(
        self,
        accountId=None,
        orderId=None,
        maxResults=-1,
        fromEnteredTime=None,
        toEnteredTime=None,
        status=None,
    ):
        """get order

        Args:
            accountId (int): account id
            orderId (int): orderId
            maxResults (int): max number of results to return
            fromEnteredTime (str): yyyy-MM-dd to filter by
            toEnteredTime (str): yyyy-MM-dd to filter by
            status (str): only return orders with this status
        """
        params = {}
        if status and status not in STATUS_VALUES:
            raise TDAAPIError("Status must be in {}".format(STATUS_VALUES))
        elif status:
            params["status"] = status

        if accountId:
            params["accountId"] = accountId
        if orderId:
            params["orderId"] = orderId
        if maxResults:
            params["maxResults"] = maxResults
        if fromEnteredTime:
            params["fromEnteredTime"] = fromEnteredTime
        if toEnteredTime:
            params["toEnteredTime"] = toEnteredTime
        return self._request(GET_ORDER_BY_QUERY, json=params).json()

    def cancelOrder(self, accountId, orderId):
        """cancel the given order

        Args:
            accountId (int): account id the order is under
            orderId (int): order id of order to cancel
        """
        return self._request(
            CANCEL_ORDER.format(accountId=accountId, orderId=orderId), method="DELETE"
        )

    def placeOrder(self, accountId, order):
        """place an order

        Args:
            accountId (int): id of account to place order under
            order (JSON): order instance to place
        """
        return self._request(
            PLACE_ORDER.format(accountId=accountId), method="POST", json=order
        )

    def replaceOrder(self, accountId, orderId, order):
        """place an order

        Args:
            accountId (int): id of account to place order under
            orderId (int): id of order to replace
            order (JSON): order instance to place
        """
        return self._request(
            REPLACE_ORDER.format(accountId=accountId, orderId=orderId),
            method="PUT",
            data=order,
        ).json()

    def savedOrders(self, accountId=None, savedOrderId=None):
        """get saved orders

        Args:
            accountId (int): id of account to get saved orders from
            savedOrderId (int): id of saved order
        """
        if not accountId and savedOrderId:
            raise TDAAPIError(
                "Must provide account id if attempting to lookup by savedOrderId"
            )

        if not accountId:
            ret = {}
            for account in self.accountIds:
                ret[account] = self._request(
                    GET_SAVED_ORDER_BY_PATH.format(accountId=account)
                ).json()
            return ret

        if savedOrderId:
            return self._request(
                GET_SAVED_ORDER.format(accountId=accountId, savedOrderId=savedOrderId)
            ).json()
        return self._request(GET_SAVED_ORDER_BY_PATH.format(accountId=accountId)).json()

    def createSavedOrder(self, accountId, order):
        """create a saved order

        Args:
            accountId (int): id of account to place order under
            order (JSON): order instance to place
        """
        return self._request(
            CREATE_SAVED_ORDER.format(accountId=accountId), method="POST", data=order
        ).json()

    def deleteSavedOrder(self, accountId, savedOrderId):
        """delete a saved order

        Args:
            accountId (int): id of account to place order under
            savedOrderId (int): id of order instance to delete
        """
        return self._request(
            DELETE_SAVED_ORDER.format(accountId=accountId, savedOrderId=savedOrderId),
            method="DELETE",
        ).json()

    def replaceSavedOrder(self, accountId, savedOrderId, order):
        """create a saved order

        Args:
            accountId (int): id of account to place order under
            savedOrderId (int): id of order instance to delete
            order (JSON): order instance to place
        """
        return self._request(
            REPLACE_SAVED_ORDER.format(accountId=accountId, savedOrderId=savedOrderId),
            method="PUT",
            data=order,
        ).json()

    def hours(self, market="EQUITY", date=None):
        """get market hours

        Args:
            market (str): market to get hours for, in ('EQUITY', 'OPTION', 'FUTURE', 'BOND', 'FOREX')
            date (str): date to get hours for, yyyy-MM-dd or yyyy-MM-dd'T'HH:mm::ssz
        """
        if date:
            params = {"date": date}
        else:
            params = {}

        if market:
            if market not in MARKETS_VALUES:
                raise TDAAPIError("Markets must be in {}".format(MARKETS_VALUES))
            return self._request(
                GET_HOURS_FOR_SINGLE_MARKET.format(market=market), params=params
            ).json()
        return self._request(GET_HOURS_FOR_MULTIPLE_MARKETS, params=params).json()

    def preferences(self, accountId=None):
        """get preferences for account

        Args:
            accountId (int): account to get preferences for
        """
        if not accountId:
            ret = {}
            for account in self.accountIds:
                ret[account] = self._request(
                    GET_PREFERENCES.format(accountId=account)
                ).json()
            return ret
        return self._request(GET_PREFERENCES.format(accountId=accountId)).json()

    def updatePreferences(self, accountId, preferences):
        """update preferences for account

        Args:
            accountId (int): account to get preferences for
            preferences (JSON): preferences to update
        """
        return self._request(
            UPDATE_PREFERENCES.format(accountId=accountId),
            method="PUT",
            data=preferences,
        ).json()

    def watchlists(self, accountId=None, watchlistId=None):
        """get watchlist for account

        Args:
            accountId (int): account to get watchlist for
            watchlistId (int): watchlist to get
        """
        if not accountId:
            return self._request(GET_WATCHLISTS_MULTIPLE_ACCOUNTS).json()
        if watchlistId:
            return self._request(
                GET_WATCHLIST.format(accountId=accountId, watchlistId=watchlistId)
            ).json()
        return self._request(GET_WATCHLISTS.format(accountId=accountId)).json()

    def createWatchlist(self, accountId, watchlist):
        """create watchlist for account

        Args:
            accountId (int): account to get watchlist for
            watchlist (JSON): watchlist to create
        """
        return self._request(
            CREATE_WATCHLIST.format(accountId=accountId), method="POST", json=watchlist
        )

    def updateWatchlist(self, accountId, watchlistId, watchlist):
        """update watchlist for account

        Args:
            accountId (int): account to get watchlist for
            watchlistId (int): watchlist to update
            watchlist (JSON): watchlist to update with
        """
        return self._request(
            UPDATE_WATCHLIST.format(accountId=accountId, watchlistId=watchlistId),
            method="PATCH",
            json=watchlist,
        )

    def replaceWatchlist(self, accountId, watchlistId, watchlist):
        """update watchlist for account

        Args:
            accountId (int): account to get watchlist for
            watchlistId (int): watchlist to update
            watchlist (JSON): watchlist to update with
        """
        return self._request(
            REPLACE_WATCHLIST.format(accountId=accountId, watchlistId=watchlistId),
            method="PUT",
            json=watchlist,
        )

    def deleteWatchlist(self, accountId, watchlistId):
        """delete watchlist for account

        Args:
            accountId (int): account to delete watchlist from
            watchlistId (int): watchlist to delete
        """
        return self._request(
            DELETE_WATCHLIST.format(accountId=accountId, watchlistId=watchlistId),
            method="DELETE",
        )
