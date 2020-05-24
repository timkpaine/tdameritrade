class OrderActivity:
    pass


class Execution(OrderActivity):
    def __init__(self):
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
