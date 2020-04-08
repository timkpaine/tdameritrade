STATUS = (
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
    'EXPIRED',
)


SESSION = (
    'NORMAL',
    'AM',
    'PM',
    'SEAMLESS',
)


DURATION = (
    'DAY',
    'GOOD_TILL_CANCEL',
    'FILL_OR_KILL',
)

ORDER_TYPE = (
    'MARKET',
    'LIMIT',
    'STOP',
    'STOP_LIMIT',
    'TRAILING_STOP',
    'MARKET_ON_CLOSE',
    'EXERCISE',
    'TRAILING_STOP_LIMIT',
    'NET_DEBIT',
    'NET_CREDIT',
    'NET_ZERO',
)


COMPLEX_ORDER_STRATEGY_TYPE = (
    'TRAILING_STOP',
    'MARKET_ON_CLOSE',
    'EXERCISE',
    'TRAILING_STOP_LIMIT',
    'NET_DEBIT',
    'NET_CREDIT',
    'NET_ZERO',
)


DESTINATION = (
    'INET',
    'ECN_ARCA',
    'CBOE',
    'AMEX',
    'PHLX',
    'ISE',
    'BOX',
    'NYSE',
    'NASDAQ',
    'BATS',
    'C2',
    'AUTO',
)

LINK_BASIS = (
    'MANUAL',
    'BASE',
    'TRIGGER',
    'LAST',
    'BID',
    'ASK',
    'ASK_BID',
    'MARK',
    'AVERAGE',
)

LINK_TYPE = (
    'VALUE',
    'PERCENT',
    'TICK',
)

STOP_TYPE = (
    'STANDARD',
    'BID',
    'ASK',
    'LAST',
    'MARK',
)

TAX_LOT_METHOD = (
    'FIFO',
    'LIFO',
    'HIGH_COST',
    'LOW_COST',
    'AVERAGE_COST',
    'SPECIFIC_LOT',
)

LEG_TYPE = (
    'EQUITY',
    'OPTION',
    'INDEX',
    'MUTUAL_FUND',
    'CASH_EQUIVALENT',
    'FIXED_INCOME',
    'CURRENCY',
)

INSTRUCTION = (
    'BUY',
    'SELL',
    'BUY_TO_COVER',
    'SELL_TO_COVER',
    'SELL_SHORT',
    'BUY_TO_OPEN',
    'BUY_TO_CLOSE',
    'SELL_TO_OPEN',
    'SELL_TO_CLOSE',
    'EXCHANGE',
)

POSITON_EFFECT = (
    'OPENING',
    'CLOSING',
    'AUTOMATIC',
)


QUANTITY_TYPE = (
    'ALL_SHARES',
    'DOLLARS',
    'SHARES',
)

SPECIAL_INSTRUCTION = (
    'ALL_OR_NONE',
    'DO_NOT_REDUCE',
    'ALL_OR_NONE_DO_NOT_REDUCE',
)

ORDER_STRATEGY_TYPE = (
    'SINGLE',
    'OCO',
    'TRIGGER',
)

OPTION_TYPE = (
    'VANILLA',
    'BINARY',
    'BARRIER',
)

PUT_CALL = (
    'PUT',
    'CALL',
)

MUTUAL_FUND_TYPE = (
    'NOT_APPLICABLE',
    'OPEN_END_NON_TAXABLE',
    'OPEN_END_TAXABLE',
    'NO_LOAD_NON_TAXABLE',
    'NO_LOAD_TAXABLE',
)


CASH_EQUIVALENT_TYPE = (
    'SAVINGS',
    'MONEY_MARKET_FUND',
)
