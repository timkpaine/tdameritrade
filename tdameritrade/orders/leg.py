"""
Order Leg usedin in Orders API
"""
from dataclasses import dataclass
from .base import BaseOrder
from .instruments import Instrument
from .constants import (
    OrderLegType,
    Instruction,
    PositionEffect,
    QuantityType,
)


@dataclass
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
