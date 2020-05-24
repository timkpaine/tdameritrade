from .base import BaseOrder


class OrderActivity(BaseOrder):
    pass


class Execution(OrderActivity):
    """
    activityType: 'EXECUTION' or 'ORDER_ACTION',
    executionType: 'FILL',
    quantity: 0,
    orderRemainingQuantity: 0,
    executionLegs: [
        {
            legId: 0,
            quantity: 0,
            mismarkedQuantity: 0,
            price: 0,
            time: string
        }
    ]
    """


class ExecutionLeg(OrderActivity):
    """
    legId: 0,
    quantity: 0,
    mismarkedQuantity: 0,
    price: 0,
    time: string
    """
    fields = [
        "legId",
        "quantity",
        "mismarkedQuantity",
        "price",
        "time",
    ]
