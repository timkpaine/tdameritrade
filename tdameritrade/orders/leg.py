"""
Order Leg usedin in Orders API
"""
from dataclasses import dataclass

from .base import BaseOrder
from .constants import Instruction, OrderLegType, PositionEffect, QuantityType
from .instruments import Instrument


@dataclass(frozen=True)
class OrderLeg(BaseOrder):
    """OrderLeg used in orderLegCollection
    """

    orderLegType: OrderLegType = None
    legId: int = None
    instrument: Instrument = None
    instruction: Instruction = None
    positionEffect: PositionEffect = None
    quantity: int = None
    quantityType: QuantityType = None
