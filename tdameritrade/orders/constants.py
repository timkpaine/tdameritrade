"""Constants used in Orders
"""
from enum import Enum as _Enum


class _ExtendedEnum(_Enum):
    """
    Base Enum class used by all order Enums.
    """
    @classmethod
    def list(cls):
        """Lists all values in Enum

        Found here: https://stackoverflow.com/questions/29503339/how-to-get-all-values-from-python-enum-class/54919285#54919285
        """
        return list(map(lambda c: c.value, cls))


class Session(_ExtendedEnum):
    NORMAL = "NORMAL"
    AM = "AM"
    PM = "PM"
    SEAMLESS = "SEAMLESS"


class Duration(_ExtendedEnum):
    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"
    FILL_OR_KILL = "FILL_OR_KILL"


class OrderType(_ExtendedEnum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    EXERCISE = "EXERCISE"
    TRAILING_STOP_LIMIT = "TRAILING_STOP_LIMIT"
    NET_DEBIT = "NET_DEBIT"
    NET_CREDIT = "NET_CREDIT"
    NET_ZERO = "NET_ZERO"


class ComplexOrderStrategyType(_ExtendedEnum):
    NONE = "NONE"
    COVERED = "COVERED"
    VERTICAL = "VERTICAL"
    BACK_RATIO = "BACK_RATIO"
    CALENDAR = "CALENDAR"
    DIAGONAL = "DIAGONAL"
    STRADDLE = "STRADDLE"
    STRANGLE = "STRANGLE"
    COLLAR_SYNTHETIC = "COLLAR_SYNTHETIC"
    BUTTERFLY = "BUTTERFLY"
    CONDOR = "CONDOR"
    IRON_CONDOR = "IRON_CONDOR"
    VERTICAL_ROLL = "VERTICAL_ROLL"
    COLLAR_WITH_STOCK = "COLLAR_WITH_STOCK"
    DOUBLE_DIAGONAL = "DOUBLE_DIAGONAL"
    UNBALANCED_BUTTERFLY = "UNBALANCED_BUTTERFLY"
    UNBALANCED_CONDOR = "UNBALANCED_CONDOR"
    UNBALANCED_IRON_CONDOR = "UNBALANCED_IRON_CONDOR"
    UNBALANCED_VERTICAL_ROLL = "UNBALANCED_VERTICAL_ROLL"
    CUSTOM = "CUSTOM"


class RequestedDestination(_ExtendedEnum):
    INET = "INET"
    ECN_ARCA = "ECN_ARCA"
    CBOE = "CBOE"
    AMEX = "AMEX"
    PHLX = "PHLX"
    ISE = "ISE"
    BOX = "BOX"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    BATS = "BATS"
    C2 = "C2"
    AUTO = "AUTO"


class StopPriceLinkBasis(_ExtendedEnum):
    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"


class StopPriceLinkType(_ExtendedEnum):
    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"


class StopType(_ExtendedEnum):
    STANDARD = "STANDARD"
    BID = "BID"
    ASK = "ASK"
    LAST = "LAST"
    MARK = "MARK"


class PriceLinkBasis(_ExtendedEnum):
    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"


class PriceLinkType(_ExtendedEnum):
    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"


class TaxLotMethod(_ExtendedEnum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    HIGH_COST = "HIGH_COST"
    LOW_COST = "LOW_COST"
    AVERAGE_COST = "AVERAGE_COST"
    SPECIFIC_LOT = "SPECIFIC_LOT"


class OrderLegType(_ExtendedEnum):
    EQUITY = "EQUITY"
    OPTION = "OPTION"
    INDEX = "INDEX"
    MUTUAL_FUND = "MUTUAL_FUND"
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    FIXED_INCOME = "FIXED_INCOME"
    CURRENCY = "CURRENCY"


class Instruction(_ExtendedEnum):
    BUY = "BUY"
    SELL = "SELL"
    BUY_TO_COVER = "BUY_TO_COVER"
    SELL_SHORT = "SELL_SHORT"
    BUY_TO_OPEN = "BUY_TO_OPEN"
    BUY_TO_CLOSE = "BUY_TO_CLOSE"
    SELL_TO_OPEN = "SELL_TO_OPEN"
    SELL_TO_CLOSE = "SELL_TO_CLOSE"
    EXCHANGE = "EXCHANGE"


class PositionEffect(_ExtendedEnum):
    OPENING = "OPENING"
    CLOSING = "CLOSING"
    AUTOMATIC = "AUTOMATIC"


class QuantityType(_ExtendedEnum):
    ALL_SHARES = "ALL_SHARES"
    DOLLARS = "DOLLARS"
    SHARES = "SHARES"


class SpecialInstruction(_ExtendedEnum):
    ALL_OR_NONE = "ALL_OR_NONE"
    DO_NOT_REDUCE = "DO_NOT_REDUCE"
    ALL_OR_NONE_DO_NOT_REDUCE = "ALL_OR_NONE_DO_NOT_REDUCE"


class OrderStrategyType(_ExtendedEnum):
    SINGLE = "SINGLE"
    OCO = "OCO"
    TRIGGER = "TRIGGER"


class Status(_ExtendedEnum):
    AWAITING_PARENT_ORDER = "AWAITING_PARENT_ORDER"
    AWAITING_CONDITION = "AWAITING_CONDITION"
    AWAITING_MANUAL_REVIEW = "AWAITING_MANUAL_REVIEW"
    ACCEPTED = "ACCEPTED"
    AWAITING_UR_OUT = "AWAITING_UR_OUT"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    QUEUED = "QUEUED"
    WORKING = "WORKING"
    REJECTED = "REJECTED"
    PENDING_CANCEL = "PENDING_CANCEL"
    CANCELED = "CANCELED"
    PENDING_REPLACE = "PENDING_REPLACE"
    REPLACED = "REPLACED"
    FILLED = "FILLED"
    EXPIRED = "EXPIRED"

