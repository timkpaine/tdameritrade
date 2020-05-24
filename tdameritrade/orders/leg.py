"""
Order Leg usedin in Orders API
"""
from .base import BaseOrder


class OrderLeg(BaseOrder):
    """
    orderLegType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY',
    legId: 0,
    instrument: The type <Instrument> has the following subclasses [Equity, FixedIncome, MutualFund, CashEquivalent, Option],
    instruction: 'BUY' or 'SELL' or 'BUY_TO_COVER' or 'SELL_SHORT' or 'BUY_TO_OPEN' or 'BUY_TO_CLOSE' or 'SELL_TO_OPEN' or 'SELL_TO_CLOSE' or 'EXCHANGE',
    positionEffect: 'OPENING' or 'CLOSING' or 'AUTOMATIC',
    quantity: 0,
    quantityType: 'ALL_SHARES' or 'DOLLARS' or 'SHARES'
    """
