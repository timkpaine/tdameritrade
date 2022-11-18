from .constants import (
    ComplexOrderStrategyType,
    Duration,
    Instruction,
    OrderStrategyType,
    OrderType,
    Session,
)
from .leg_builder import create_equity_order_leg, create_option_order_leg
from .models.orders import Order


def build_buy_market_stock_order(symbol, quantity):
    """Build Buy Market Stock Order

    Buy {quantity} shares of {symbol} at the Market good for the Day.

    Simple sample from https://developer.tdameritrade.com/content/place-order-samples

    Args:
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


def build_buy_limit_option_order(symbol, quantity, price):
    """Build Buy Limit: Single Option

    Buy to open {quantity} contracts of the {symbol with date and option info}
    at a Limit of {price} good for the Day.

    Args:
        symbol: symbol you want to trade.  Includes date e.g., XYZ_032015C49
        quantity: Amount you want to buy
        price: Amount you want to buy the option for

    Note:
        May want to add expiry date and type of option (CALL, PUT) and
        create completed symbol
    """
    # Constants
    complex_order_strategy_type = ComplexOrderStrategyType.NONE
    order_type = OrderType.LIMIT
    session = Session.NORMAL
    duration = Duration.DAY
    order_strategy_type = OrderStrategyType.SINGLE
    _instruction = Instruction.BUY_TO_OPEN

    _order_leg = create_option_order_leg(
        instruction=_instruction,
        quantity=quantity,
        symbol=symbol,
    )
    order_leg_collection = [_order_leg]

    return Order(
        complexOrderStrategyType=complex_order_strategy_type,
        orderType=order_type,
        session=session,
        price=price,
        duration=duration,
        orderStrategyType=order_strategy_type,
        orderLegCollection=order_leg_collection,
    )


def build_buy_limit_vertical_call_spread_order(
    buy_symbol, sell_symbol, quantity, price
):
    """Buy Limit: Vertical Call Spread

    Buy to open 10 contracts of the XYZ Jan 15, 2016 $40 Call and
    Sell to open 10 contracts of the XYZ Jan 15, 2016 $42.5 Call
    for a Net Debit of $1.20 good for the Day.

    Args:
        buy_symbol: symbol you want to buy.  Includes date e.g., XYZ_011516C40
        sell_symbol: symbol you want to buy.  Includes date e.g., XYZ_011516C42.5
        quantity: Amount you want to buy.
        price: Amount you want to buy the spread for
    """
    # Constants
    order_type = OrderType.NET_DEBIT
    session = Session.NORMAL
    duration = Duration.DAY
    order_strategy_type = OrderStrategyType.SINGLE

    _buy_order_leg = create_option_order_leg(
        instruction=Instruction.BUY_TO_OPEN,
        quantity=quantity,
        symbol=buy_symbol,
    )

    _sell_order_leg = create_option_order_leg(
        instruction=Instruction.SELL_TO_OPEN,
        quantity=quantity,
        symbol=sell_symbol,
    )

    order_leg_collection = [
        _buy_order_leg,
        _sell_order_leg,
    ]

    return Order(
        orderType=order_type,
        session=session,
        price=price,
        duration=duration,
        orderStrategyType=order_strategy_type,
        orderLegCollection=order_leg_collection,
    )


def build_custom_option_spread_order(
    buy_symbol, sell_symbol, buy_quantity, sell_quantity
):
    """Custom Option Spread

    Buy to open 2 contracts of the XYZ Jan 17, 2020 $43 Put and Sell to open
    1 contracts of the XYZ Jan 18, 2019 $45 Put at the Market good for the Day.
    """
    # Constants
    order_strategy_type = OrderStrategyType.SINGLE
    order_type = OrderType.MARKET
    session = Session.NORMAL
    duration = Duration.DAY
    complex_order_strategy_type = ComplexOrderStrategyType.CUSTOM

    _buy_order_leg = create_option_order_leg(
        instruction=Instruction.BUY_TO_OPEN,
        quantity=buy_quantity,
        symbol=buy_symbol,
    )

    _sell_order_leg = create_option_order_leg(
        instruction=Instruction.SELL_TO_OPEN,
        quantity=sell_quantity,
        symbol=sell_symbol,
    )

    order_leg_collection = [
        _sell_order_leg,
        _buy_order_leg,
    ]

    return Order(
        orderStrategyType=order_strategy_type,
        orderType=order_type,
        orderLegCollection=order_leg_collection,
        complexOrderStrategyType=complex_order_strategy_type,
        duration=duration,
        session=session,
    )
