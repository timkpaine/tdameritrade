import os
import requests
import pandas as pd

from tdameritrade.auth import refresh_token
from .urls import ACCOUNTS, INSTRUMENTS, QUOTES, SEARCH, HISTORY, OPTIONCHAIN, MOVERS, ORDERS, ORDER


class TDClient(object):
    def __init__(self, access_token=None, accountIds=None, refresh_token=None, client_id=None):
        self._token = access_token or os.environ.get('ACCESS_TOKEN')
        self.accountIds = accountIds or []
        self.refresh_token = refresh_token or os.environ['REFRESH_TOKEN']
        self.client_id = client_id or os.environ['CLIENT_ID']

    def _headers(self):
        return {'Authorization': 'Bearer ' + self._token}

    def _request(self, url, method='GET', *args, **kwargs):
        attempts = 0
        while attempts <= 1:
            resp = requests.request(method=method, url=url, headers=self._headers(),
                                    *args, **kwargs)
            if resp.status_code == 401:
                attempts += 1
                self._token = refresh_token(self.refresh_token, self.client_id)['access_token']
            else:
                return resp
        resp.raise_for_status()

    def accounts(self, positions=False, orders=False):
        ret = {}

        if positions or orders:
            fields = '?fields='
            if positions:
                fields += 'positions'
                if orders:
                    fields += ',orders'
            elif orders:
                fields += 'orders'
        else:
            fields = ''

        if self.accountIds:
            for acc in self.accountIds:
                resp = self._request(ACCOUNTS + str(acc) + fields)
                if resp.status_code == 200:
                    ret[acc] = resp.json()
                else:
                    raise Exception(resp.text)
        else:
            resp = self._request(ACCOUNTS + fields)
            if resp.status_code == 200:
                for account in resp.json():
                    ret[account['securitiesAccount']['accountId']] = account
            else:
                raise Exception(resp.text)
        return ret

    def accountsDF(self):
        return pd.io.json.json_normalize(self.accounts())

    def search(self, symbol, projection='symbol-search'):
        return self._request(SEARCH,
                             params={'symbol': symbol,
                                     'projection': projection}).json()

    def searchDF(self, symbol, projection='symbol-search'):
        ret = []
        dat = self.search(symbol, projection)
        for symbol in dat:
            ret.append(dat[symbol])
        return pd.DataFrame(ret)

    def fundamental(self, symbol):
        return self.search(symbol, 'fundamental')

    def fundamentalDF(self, symbol):
        return self.searchDF(symbol, 'fundamental')

    def instrument(self, cusip):
        return self._request(INSTRUMENTS + str(cusip)).json()

    def instrumentDF(self, cusip):
        return pd.DataFrame(self.instrument(cusip))

    def quote(self, symbol):
        return self._request(QUOTES,
                             params={'symbol': symbol.upper()}).json()

    def quoteDF(self, symbol):
        x = self.quote(symbol)
        return pd.DataFrame(x).T.reset_index(drop=True)

    def history(self, symbol):
        return self._request(HISTORY % symbol).json()

    def historyDF(self, symbol):
        x = self.history(symbol)
        df = pd.DataFrame(x['candles'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        return df

    def options(self, symbol):
        return self._request(OPTIONCHAIN,
                             params={'symbol': symbol.upper()}).json()

    def optionsDF(self, symbol):
        ret = []
        dat = self.options(symbol)
        for date in dat['callExpDateMap']:
            for strike in dat['callExpDateMap'][date]:
                ret.extend(dat['callExpDateMap'][date][strike])
        for date in dat['putExpDateMap']:
            for strike in dat['putExpDateMap'][date]:
                ret.extend(dat['putExpDateMap'][date][strike])

        df = pd.DataFrame(ret)
        for col in ('tradeTimeInLong', 'quoteTimeInLong', 'expirationDate', 'lastTradingDay'):
            df[col] = pd.to_datetime(df[col], unit='ms')
        return df

    def movers(self, index, direction='up', change_type='percent'):
        return self._request(MOVERS % index,
                             params={'direction': direction,
                                     'change_type': change_type})

    def trade_options(self, account_id, legs, quantity, price=None,
                      strategy='NONE', order_type='MARKET',
                      duration='DAY', session='NORMAL'):
        data = {
            "session": session,
            "duration": duration,
            "orderType": order_type,
            "orderStrategyType": "SINGLE",
            "orderLegCollection": legs,
            "quantity": quantity,
            "complexOrderStrategyType": strategy,
        }
        if price:
            data['price'] = str(price)
        resp = self._request(ORDERS % account_id, 'POST', json=data)
        resp.raise_for_status()
        return self._request(resp.headers['Location']).json()
