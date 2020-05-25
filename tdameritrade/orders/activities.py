from .base import BaseOrder
from typing import List
from .constants import ActivityType, ExecutionType
from dataclasses import dataclass


@dataclass
class OrderActivity(BaseOrder):
    pass


@dataclass
class ExecutionLeg(OrderActivity):
    """ExecutionLeg using in Execution
    """

    legId: int = None
    quantity: int = None
    mismarkedQuantity: int = None
    price: int = None
    time: str = None


@dataclass
class Execution(OrderActivity):
    """Execution
    """

    activityType: ActivityType = None
    executionType: ExecutionType = None
    quantity: int = None
    orderRemainingQuantity: int = None
    executionLegs: List[ExecutionLeg] = None
