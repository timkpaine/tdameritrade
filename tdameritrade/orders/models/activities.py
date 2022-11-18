from dataclasses import dataclass
from typing import List

from ..constants import ActivityType, ExecutionType
from .base import BaseOrder


@dataclass
class OrderActivity(BaseOrder):
    pass


@dataclass
class ExecutionLeg(BaseOrder):
    """ExecutionLeg used in Execution"""

    legId: int = None
    quantity: int = None
    mismarkedQuantity: int = None
    price: int = None
    time: str = None


@dataclass
class Execution(OrderActivity):
    """Execution"""

    activityType: ActivityType = None
    executionType: ExecutionType = None
    quantity: int = None
    orderRemainingQuantity: int = None
    executionLegs: List = None  # List[ExecutionLeg]. Issue with List[type] formatting
