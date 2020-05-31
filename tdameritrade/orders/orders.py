from .base import BaseOrder
from dataclasses import dataclass
from typing import List, Any
from .leg import OrderLeg, create_equity_order_leg
from .activities import OrderActivity
from .constants import (
    Instruction,
    OrderLegType,
    PositionEffect,
    QuantityType,
    InstrumentAssetType,
    Session,
    Duration,
    OrderType,
    ComplexOrderStrategyType,RequestedDestination,StopPriceLinkBasis,StopPriceLinkType, StopType,PriceLinkBasis,PriceLinkType,TaxLotMethod, SpecialInstruction, OrderStrategyType, Status
)
from .instruments import Instrument, EquityInstrument, OptionInstrument


@dataclass
class CancelTime(BaseOrder):
    date: str
    shortFormat: bool


@dataclass
class Order(BaseOrder):
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
    price: int = None
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



def build_buy_market_stock_order(symbol, quantity):
    """Build Buy Market Stock Order
    
    Simple sample from https://developer.tdameritrade.com/content/place-order-samples

    Args:
        instruction: Buy or Sell
        symbol: symbol you want to trade
        quantity: How much of the stock to trade
    """
    # Constants
    order_type = OrderType.MARKET
    session = Session.NORMAL
    duration = Duration.DAY
    order_strategy_type = OrderStrategyType.SINGLE
    # Can be changed to handle Buy and Sell for Equities
    _instruction = Instruction.BUY
    # Can be changed to handle options
    _instrument_asset_type = InstrumentAssetType.EQUITY  

    _order_leg = create_equity_order_leg(
        instruction=_instruction,
        quantity=quantity,
        symbol=symbol,
    )
    order_leg_collection = [_order_leg]

    return Order(
        orderType=order_type,
        session=session,
        duration=duration,
        orderStrategyType=order_strategy_type,
        orderLegCollection=order_leg_collection,
    )
