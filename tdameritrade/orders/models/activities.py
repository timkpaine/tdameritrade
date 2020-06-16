from dataclasses import dataclass
from typing import List, Any

from .base import BaseOrder
from ..constants import ActivityType, ExecutionType


@dataclass
class OrderActivity(BaseOrder):
    pass


@dataclass(frozen=True)
class ExecutionLeg(BaseOrder):
    """ExecutionLeg used in Execution
    """

    legId: int = None
    quantity: int = None
    mismarkedQuantity: int = None
    price: int = None
    time: str = None


@dataclass(frozen=True)
class Execution(OrderActivity):
    """Execution
    """

    activityType: ActivityType = None
    executionType: ExecutionType = None
    quantity: int = None
    orderRemainingQuantity: int = None
    executionLegs: List = None  # List[ExecutionLeg]. Issue with List[type] formatting
