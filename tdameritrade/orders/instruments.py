import json


class _InstrumentEncoder(json.JSONEncoder):
    def default(self, o):
        return o.kwargs


class _Instrument:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def json(self):
        return json.dumps(self.kwargs, cls=_InstrumentEncoder)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {str(self)}>"

    def __str__(self):
        return str(self.kwargs)


class Equity(_Instrument):
    """Equity Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
    """


class FixedIncome(_Instrument):
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


class MutualFund(_Instrument):
    """Mutual Fund Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
        type: 'NOT_APPLICABLE' or 'OPEN_END_NON_TAXABLE' or 'OPEN_END_TAXABLE' or 'NO_LOAD_NON_TAXABLE' or 'NO_LOAD_TAXABLE'
    """


class CashEquivalent(_Instrument):
    """Cash Equivalent Instrument

    Keyword Args:
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
        cusip: string
        symbol: string
        description: string
        type: 'SAVINGS' or 'MONEY_MARKET_FUND'
    """


class Option(_Instrument):
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


class OptionDeliverable(_Instrument):
    """Option Deliverable in Option's optionDeliverables list
    Keyword Args:
        symbol: string
        deliverableUnits: 0
        currencyType: 'USD' or 'CAD' or 'EUR' or 'JPY'
        assetType: 'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'
    """
