"""Constants used in Orders
"""
from enum import Enum


class ExtendedConstant(str, Enum):
    """
    Base Enum class used by all order Enums.
    """

    @classmethod
    def list(cls):
        """Lists all values in Enum

        Found here: https://stackoverflow.com/questions/29503339/how-to-get-all-values-from-python-enum-class/54919285#54919285
        """
        return list(map(lambda c: c.value, cls))


class Session(ExtendedConstant):
    NORMAL = "NORMAL"
    AM = "AM"
    PM = "PM"
    SEAMLESS = "SEAMLESS"


class Duration(ExtendedConstant):
    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"
    FILL_OR_KILL = "FILL_OR_KILL"


class OrderType(ExtendedConstant):
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


class ComplexOrderStrategyType(ExtendedConstant):
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


class RequestedDestination(ExtendedConstant):
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


class StopPriceLinkBasis(ExtendedConstant):
    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"


class StopPriceLinkType(ExtendedConstant):
    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"


class StopType(ExtendedConstant):
    STANDARD = "STANDARD"
    BID = "BID"
    ASK = "ASK"
    LAST = "LAST"
    MARK = "MARK"


class PriceLinkBasis(ExtendedConstant):
    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"


class PriceLinkType(ExtendedConstant):
    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"


class TaxLotMethod(ExtendedConstant):
    FIFO = "FIFO"
    LIFO = "LIFO"
    HIGH_COST = "HIGH_COST"
    LOW_COST = "LOW_COST"
    AVERAGE_COST = "AVERAGE_COST"
    SPECIFIC_LOT = "SPECIFIC_LOT"


class SpecialInstruction(ExtendedConstant):
    ALL_OR_NONE = "ALL_OR_NONE"
    DO_NOT_REDUCE = "DO_NOT_REDUCE"
    ALL_OR_NONE_DO_NOT_REDUCE = "ALL_OR_NONE_DO_NOT_REDUCE"


class OrderStrategyType(ExtendedConstant):
    SINGLE = "SINGLE"
    OCO = "OCO"
    TRIGGER = "TRIGGER"


class Status(ExtendedConstant):
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


# Order Leg Constants


class OrderLegType(ExtendedConstant):
    EQUITY = "EQUITY"
    OPTION = "OPTION"
    INDEX = "INDEX"
    MUTUAL_FUND = "MUTUAL_FUND"
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    FIXED_INCOME = "FIXED_INCOME"
    CURRENCY = "CURRENCY"


class Instruction(ExtendedConstant):
    BUY = "BUY"
    SELL = "SELL"
    BUY_TO_COVER = "BUY_TO_COVER"
    SELL_SHORT = "SELL_SHORT"
    BUY_TO_OPEN = "BUY_TO_OPEN"
    BUY_TO_CLOSE = "BUY_TO_CLOSE"
    SELL_TO_OPEN = "SELL_TO_OPEN"
    SELL_TO_CLOSE = "SELL_TO_CLOSE"
    EXCHANGE = "EXCHANGE"


class PositionEffect(ExtendedConstant):
    OPENING = "OPENING"
    CLOSING = "CLOSING"
    AUTOMATIC = "AUTOMATIC"


class QuantityType(ExtendedConstant):
    ALL_SHARES = "ALL_SHARES"
    DOLLARS = "DOLLARS"
    SHARES = "SHARES"


# Activity Enums


class ActivityType(ExtendedConstant):
    EXECUTION = "EXECUTION"
    ORDER_ACTION = "ORDER_ACTION"


class ExecutionType(ExtendedConstant):
    FILL = "FILL"


# Instrument Enums


class InstrumentAssetType(ExtendedConstant):
    EQUITY = "EQUITY"
    OPTION = "OPTION"
    INDEX = "INDEX"
    MUTUAL_FUND = "MUTUAL_FUND"
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    FIXED_INCOME = "FIXED_INCOME"
    CURRENCY = "CURRENCY"


class MutualFundType(ExtendedConstant):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    OPEN_END_NON_TAXABLE = "OPEN_END_NON_TAXABLE"
    OPEN_END_TAXABLE = "OPEN_END_TAXABLE"
    NO_LOAD_NON_TAXABLE = "NO_LOAD_NON_TAXABLE"
    NO_LOAD_TAXABLE = "NO_LOAD_TAXABLE"


class CashEquivalentType(ExtendedConstant):
    SAVINGS = "SAVINGS"
    MONEY_MARKET_FUND = "MONEY_MARKET_FUND"


class OptionType(ExtendedConstant):
    VANILLA = "VANILLA"
    BINARY = "BINARY"
    BARRIER = "BARRIER"


class OptionPutCall(ExtendedConstant):
    PUT = "PUT"
    CALL = "CALL"


class OptionDeliverableCurrencyType(ExtendedConstant):
    USD = "USD"
    CAD = "CAD"
    EUR = "EUR"
    JPY = "JPY"
