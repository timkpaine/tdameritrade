from .base import BaseOrder


class Instrument(BaseOrder):
    pass


class Equity(Instrument):
    """Equity Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
    """


class FixedIncome(Instrument):
    """Fixed Income Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
        maturityDate: string
        variableRate: 0
        factor: 0
    """


class MutualFund(Instrument):
    """Mutual Fund Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
        type: 'NOT_APPLICABLE' or 'OPEN_END_NON_TAXABLE' or 'OPEN_END_TAXABLE' or 'NO_LOAD_NON_TAXABLE' or 'NO_LOAD_TAXABLE'
    """


class CashEquivalent(Instrument):
    """Cash Equivalent Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
        type: 'SAVINGS' or 'MONEY_MARKET_FUND'
    """


class Option(Instrument):
    """Option Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
        type: 'VANILLA' or 'BINARY' or 'BARRIER'
        putCall: 'PUT' or 'CALL'
        underlyingSymbol: string
        optionMultiplier: 0
        optionDeliverables: [
            {
                symbol: string
                deliverableUnits: 0
                currencyType: 'USD' or 'CAD' or 'EUR' or 'JPY'
                assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
            }
        ]
    """


class OptionDeliverable(Instrument):
    """Option Deliverable in Option's optionDeliverables list
    Keyword Args:
        symbol: string
        deliverableUnits: 0
        currencyType: 'USD' or 'CAD' or 'EUR' or 'JPY'
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
    """
