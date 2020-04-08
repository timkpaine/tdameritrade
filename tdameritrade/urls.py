BASE = 'https://api.tdameritrade.com/v1/'

########################
# Accounts and Trading #
########################
# https://developer.tdameritrade.com/account-access/apis

# ORDERS
CANCEL_ORDER = BASE + 'accounts/{accountId}/orders/{orderId}'  # DELETE
GET_ORDER = BASE + 'accounts/{accountId}/orders/{orderId}'  # GET
GET_ORDERS_BY_PATH = BASE + 'accounts/{accountId}/orders'  # GET
GET_ORDER_BY_QUERY = BASE + 'orders'  # GET
PLACE_ORDER = BASE + 'accounts/{accountId}/orders'  # POST
REPLACE_ORDER = BASE + 'accounts/{accountId}/orders/{orderId}'  # PUT
GET_ORDER_BY_PATH_ARGS = ('maxResults', 'fromEnteredTime', 'toEnteredTime', 'status')
GET_ORDER_BY_QUERY_ARGS = ('accountId', 'maxResults', 'fromEnteredTime', 'toEnteredTime', 'status')
STATUS_VALUES = (
    'AWAITING_PARENT_ORDER',
    'AWAITING_CONDITION',
    'AWAITING_MANUAL_REVIEW',
    'ACCEPTED',
    'AWAITING_UR_OUT',
    'PENDING_ACTIVATION',
    'QUEUED',
    'WORKING',
    'REJECTED',
    'PENDING_CANCEL',
    'CANCELED',
    'PENDING_REPLACE',
    'REPLACED',
    'FILLED',
    'EXPIRED')
# maxResults: int
# fromEnteredTime: yyyy-MM-dd
# toEnteredTime: yyyy-MM-dd
# status: STATUS_VALUES

# SAVED ORDERS
CREATE_SAVED_ORDER = BASE + 'accounts/{accountId}/savedorders'  # POST
DELETE_SAVED_ORDER = BASE + 'accounts/{accountId}/savedorders/{savedOrderId}'  # DELETE
GET_SAVED_ORDER = BASE + 'accounts/{accountId}/savedorders/{savedOrderId}'  # GET
GET_SAVED_ORDER_BY_PATH = BASE + 'accounts/{accountId}/savedorders'  # GET
REPLACE_SAVED_ORDER = BASE + 'accounts/{accountId}/savedorders/{savedOrderId}'  # PUT

# ACCOUNTS
GET_ACCOUNT = BASE + 'accounts/{accountId}'  # GET
GET_ACCOUNTS = BASE + 'accounts'  # GET

##################
# AUTHENTICATION #
##################
# https://developer.tdameritrade.com/authentication/apis
ACCESS_TOKEN = BASE + 'oauth2/token'  # POST
ACCESS_TOKEN_ARGS = ('grant_type', 'refresh_token', 'access_type', 'code', 'client_id', 'redirect_uri')

###############
# INSTRUMENTS #
###############
# https://developer.tdameritrade.com/instruments/apis
SEARCH_INSTRUMENTS = BASE + 'instruments'  # GET
SEARCH_INSTRUMENTS_ARGS = ('symbol', 'projection')
SEARCH_INSTRUMENT_PROJECTION = ('symbol-search', 'symbol-regex', 'desc-search', 'desc-regex', 'fundamental')
GET_INSTRUMENT = BASE + 'instruments/{cusip}'  # GET

################
# MARKET HOURS #
################
# https://developer.tdameritrade.com/market-hours/apis
GET_HOURS_FOR_MULTIPLE_MARKETS = BASE + 'marketdata/hours'  # GET
GET_HOURS_FOR_MULTIPLE_MARKETS_ARGS = ('markets', 'date')
MARKETS_VALUES = ('EQUITY', 'OPTION', 'FUTURE', 'BOND', 'FOREX')
GET_HOURS_FOR_SINGLE_MARKET = BASE + 'marketdata/{market}/hours'  # GET
GET_HOURS_FOR_SINGLE_MARKET_ARGS = ('date')
# date: yyyy-MM-dd or yyyy-MM-dd'T'HH:mm::ssz

##########
# MOVERS #
##########
# https://developer.tdameritrade.com/movers/apis
MOVERS = BASE + 'marketdata/{index}/movers'  # GET
MOVERS_ARGS = ('direction', 'change')
DIRECTION_VALUES = ('up', 'down')
CHANGE_VALUES = ('value', 'percent')

#################
# OPTION CHAINS #
#################
# https://developer.tdameritrade.com/option-chains/apis
GET_OPTION_CHAIN = BASE + 'marketdata/chains'  # GET
OPTION_CHAIN_ARGS = ('symbol',
                     'contractType',
                     'strikeCount',
                     'includeQuotes',
                     'strategy',
                     'interval',
                     'strike',
                     'range',
                     'fromDate',
                     'toDate',
                     'volatility',
                     'underlyingPrice',
                     'interestRate',
                     'daysToExpiration',
                     'expMonth',
                     'optionType')
CONTRACT_TYPE_VALUES = ('CALL', 'PUT', 'ALL')
STRATEGY_VALUES = ('SINGLE', 'ANALYTICAL', 'COVERED', 'VERTICAL', 'CALENDAR', 'STRANGLE', 'STRADDLE', 'BUTTERFLY', 'CONDOR', 'DIAGONAL', 'COLLAR', 'ROLL')
RANGE_VALUES = ('ITM', 'NTM', 'OTM', 'SAK', 'SBK', 'SNK', 'ALL')
OPTION_TYPE_VALUES = ('S', 'NS', 'ALL')
OPTION_EXPMONTH_VALUES = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ALL')

#################
# PRICE HISTORY #
#################
# https://developer.tdameritrade.com/price-history/apis
GET_PRICE_HISTORY = BASE + 'marketdata/{symbol}/pricehistory'  # GET
GET_PRICE_HISTORY_ARGS = ('periodType',
                          'period',
                          'frequencyType',
                          'frequency',
                          'endDate',
                          'startDate',
                          'needExtendedHoursData')
PERIOD_TYPE_VALUES = ('day', 'month', 'year', 'ytd')
FREQUENCY_TYPE_VALUES = ('minute', 'daily', 'weekly', 'monthly')

##########
# QUOTES #
##########
# https://developer.tdameritrade.com/quotes/apis
GET_QUOTE = BASE + 'marketdata/{symbol}/quotes'  # GET
GET_QUOTES = BASE + 'marketdata/quotes'  # GET
GET_QUOTES_ARGS = ('symbol',)

#######################
# TRANSACTION HISTORY #
#######################
# https://developer.tdameritrade.com/transaction-history/apis
GET_TRANSACTION = BASE + 'accounts/{accountId}/transactions/{transactionId}'  # GET
GET_TRANSACTIONS = BASE + 'accounts/{accountId}/transactions'  # GET
GET_TRANSACTIONS_ARGS = ('type', 'symbol', 'startDate', 'endDate')
GET_TRANSCATION_TYPE_VALUES = ('ALL', 'TRADE', 'BUY_ONLY', 'SELL_ONLY', 'CASH_IN_OR_CASH_OUT', 'CHECKING', 'DIVIDEND', 'INTEREST', 'OTHER', 'ADVISOR_FEES')

###################
# User Info/Prefs #
###################
# https://developer.tdameritrade.com/user-principal/apis
GET_PREFERENCES = BASE + 'accounts/{accountId}/preferences'  # GET
GET_STREAMER_SUBSCRIPTION_KEYS = BASE + 'userprincipals/streamersubscriptionkeys'  # GET
GET_STREAMER_SUBSCRIPTION_KEYS_ARGS = ('accountIds',)
GET_USER_PRINCIPALS = BASE + 'userprincipals'  # GET
GET_USER_PRINCIPALS_ARGS = ('fields',)
USER_PRINCIPALS_FIELDS_VALUES = ('streamerSubscriptionKeys', 'streamerConnectionInfo', 'preferences', 'surrogateIds')
UPDATE_PREFERENCES = BASE + 'accounts/{accountId}/preferences'  # PUT

#############
# WATCHLIST #
#############
# https://developer.tdameritrade.com/watchlist/apis
CREATE_WATCHLIST = BASE + 'accounts/{accountId}/watchlists'  # POST
DELETE_WATCHLIST = BASE + 'accounts/{accountId}/watchlists/{watchlistId}'  # DELETE
GET_WATCHLIST = BASE + 'accounts/{accountId}/watchlists/{watchlistId}'  # GET
GET_WATCHLISTS_MULTIPLE_ACCOUNTS = BASE + 'accounts/watchlists'  # GET
GET_WATCHLISTS = BASE + 'accounts/{accountId}/watchlists'  # GET
REPLACE_WATCHLIST = BASE + 'accounts/{accountId}/watchlists/{watchlistId}'  # PUT
UPDATE_WATCHLIST = BASE + 'accounts/{accountId}/watchlists/{watchlistId}'  # PATCH
