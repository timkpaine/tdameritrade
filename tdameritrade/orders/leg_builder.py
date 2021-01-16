from .constants import Instruction, InstrumentAssetType
from .models.instruments import EquityInstrument, OptionInstrument
from .models.leg import OrderLeg


def create_equity_order_leg(
    instruction,
    quantity,
    symbol,
    description=None,
    cusip=None,
    **order_leg_kwargs,
):
    """Creates OrderLeg for equity orders"""
    valid_instructions = [
        Instruction("BUY"),
        Instruction("SELL"),
        Instruction("BUY_TO_COVER"),
        Instruction("SELL_SHORT"),
    ]

    asset_type = InstrumentAssetType.EQUITY

    if instruction not in valid_instructions:
        raise Exception(
            f"{instruction} not in valid instruction list for Equity Order Leg"
        )

    instrument = EquityInstrument(symbol=symbol, assetType=asset_type)
    return OrderLeg(
        instruction=instruction,
        quantity=quantity,
        instrument=instrument,
        **order_leg_kwargs,
    )


def create_option_order_leg(
    instruction,
    quantity,
    symbol,
    description=None,
    cusip=None,
    **order_leg_kwargs,
):
    """Creates Option OrderLeg"""
    asset_type = InstrumentAssetType.OPTION

    instrument = OptionInstrument(symbol=symbol, assetType=asset_type)

    return OrderLeg(
        instruction=instruction,
        quantity=quantity,
        instrument=instrument,
        **order_leg_kwargs,
    )
