import json

from tdameritrade.orders import activities
from tdameritrade.orders.constants import ActivityType, ExecutionType


def test_execution_leg_json():
    activity_type = ActivityType.EXECUTION
    execution_type = ExecutionType.FILL

    execution_leg = activities.ExecutionLeg(
        legId = 0,
        quantity = 0,
        mismarkedQuantity = 0,
        price = 0,
        time = "some_string",
    )

    actual_values = json.loads(execution_leg.json())

    for key, value in actual_values.items():
        assert execution_leg.__getattribute__(key) == value


def test_execution_json():
    activity_type = ActivityType.EXECUTION
    execution_type = ExecutionType.FILL

    execution_leg = activities.ExecutionLeg(
        legId = 0,
        quantity = 0,
        mismarkedQuantity = 0,
        price = 0,
        time = "some_string",
    )
    execution_legs = []

    execution = activities.Execution(
        activityType = activity_type,
        executionType = execution_type,
        quantity = 0,
        orderRemainingQuantity = 0,
        executionLegs = execution_legs,
    )

    actual_values = json.loads(execution.json())
    
    for key, value in actual_values.items():
        assert execution.__getattribute__(key) == value
