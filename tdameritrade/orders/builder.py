from . import constants


def upper_first_letter(string):
    """Return string with first letter in uppercase

    We can't use .title() or .capitalize() because that does .lower() on other parts of the string.
    """
    return string[0].upper() + string[1:]


# Enum Validation
enum_args = [
    "session"
    "duration"
    "orderType"
    "complexOrderStrategyType"
    "requestedDestination"
    "stopPriceLinkBasis"
    "stopPriceLinkType"
    "stopType"
    "priceLinkBasis"
    "priceLinkType"
    "taxLotMethod"
    "specialInstruction"
    "orderStrategyType"
    "status"
]

# integer validation
int_args = [
    "quantity",
    "filledQuantity",
    "remainingQuantity",
    "stopPrice",
    "stopPriceOffset",
    "price",
    "activationPrice",
    "orderId",
    "accountId",
]


def OrderBuilder(self, *, validation=True, **kwargs):
    """Builds Order dictionary to use with Orders API

    https://developer.tdameritrade.com/content/place-order-samples

    Assumption made that every field is optional
    """
    if validation:
        for key, value in kwargs:
            if key in enum_args:
                order_enum = constants.__dict__[upper_first_letter(key)]
                if value not in order_enum:
                    raise Exception(
                        f"Validation Error: {key} value {value} not in {order_enum}"
                    )
            elif key in int_args:
                try:
                    int(value)
                except Exception as err:
                    raise Exception(
                        f"Validation Error: {value} can not be cast to int - {err}"
                    )


def create_order_leg(
    *,
    orderLegType=None,
    legId=None,
    instrument=None,
    instruction=None,
    positionEffect=None,
    quantity=None,
    quantityType=None,
):
    {
        "orderLegType": "'EQUITY' or 'OPTION' or 'INDEX' or 'MUTUAL_FUND' or 'CASH_EQUIVALENT' or 'FIXED_INCOME' or 'CURRENCY'",
        "legId": 0,
        "instrument": 'The type <Instrument> has the following subclasses [Equity, FixedIncome, MutualFund, CashEquivalent, Option] descriptions are listed below"',
        "instruction": "'BUY' or 'SELL' or 'BUY_TO_COVER' or 'SELL_SHORT' or 'BUY_TO_OPEN' or 'BUY_TO_CLOSE' or 'SELL_TO_OPEN' or 'SELL_TO_CLOSE' or 'EXCHANGE'",
        "positionEffect": "'OPENING' or 'CLOSING' or 'AUTOMATIC'",
        "quantity": 0,
        "quantityType": "'ALL_SHARES' or 'DOLLARS' or 'SHARES'",
    }
