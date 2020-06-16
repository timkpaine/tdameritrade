from .base import BaseOrder
from dataclasses import dataclass
from typing import List, Any
from .leg import OrderLeg
from .activities import OrderActivity
from ..constants import (
    Session,
    Duration,
    OrderType,
    ComplexOrderStrategyType,
    RequestedDestination,
    StopPriceLinkBasis,
    StopPriceLinkType,
    StopType,
    PriceLinkBasis,
    PriceLinkType,
    TaxLotMethod,
    SpecialInstruction,
    OrderStrategyType,
    Status,
)


@dataclass
class CancelTime(BaseOrder):
    date: str = None
    shortFormat: bool = None


@dataclass
class Order(BaseOrder):
    """
    Notes:
        The int fields may not be actual ints even though the docs use an int as the default.
        When I checked the sample orders, they made price into a string e.g., "6.45".

        I made price a str for now.
    """

    session: Session = None
    duration: Duration = None
    orderType: OrderType = None
    cancelTime: CancelTime = None
    complexOrderStrategyType: ComplexOrderStrategyType = None
    quantity: int = None
    filledQuantity: int = None
    remainingQuantity: int = None
    requestedDestination: RequestedDestination = None
    destinationLinkName: str = None
    releaseTime: str = None
    stopPrice: int = None
    stopPriceLinkBasis: StopPriceLinkBasis = None
    stopPriceLinkType: StopPriceLinkType = None
    stopPriceOffset: int = None
    stopType: StopType = None
    priceLinkBasis: PriceLinkBasis = None
    priceLinkType: PriceLinkType = None
    price: str = None
    taxLotMethod: TaxLotMethod = None
    orderLegCollection: List[OrderLeg] = None
    activationPrice: int = None
    specialInstruction: SpecialInstruction = None
    orderStrategyType: OrderStrategyType = None
    orderId: int = None
    cancelable: bool = None
    editable: bool = None
    status: Status = None
    enteredTime: str = None
    closeTime: str = None
    accountId: int = None
    orderActivityCollection: List[OrderActivity] = None
    replacingOrderCollection: List[Any] = None  # Accepts list of orders
    childOrderStrategies: List[Any] = None  # Accepts list of orders
    statusDescription: str = None
