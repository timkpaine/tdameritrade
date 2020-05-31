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


def validate_order(*, validation=True, **kwargs):
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
