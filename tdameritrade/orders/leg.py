"""
Order Leg usedin in Orders API
"""
from dataclasses import dataclass

from .base import BaseOrder
from .constants import (
    Instruction,
    OrderLegType,
    PositionEffect,
    QuantityType,
    InstrumentAssetType,
)
from .instruments import Instrument, EquityInstrument, OptionInstrument


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


def create_equity_order_leg(
    instruction, quantity, symbol, description=None, cusip=None, **order_leg_kwargs,
):
    """Creates OrderLeg for equity orders
    """
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


class OptionOrderLeg(OrderLeg):
    instructions = [
        Instruction("BUY_TO_OPEN"),
        Instruction("BUY_TO_CLOSE"),
        Instruction("SELL_TO_OPEN"),
        Instruction("SELL_TO_CLOSE"),
    ]

    asset_type = InstrumentAssetType.OPTION

    def __init__(
        self,
        instruction=None,
        quantity=None,
        symbol=None,
        description=None,
        cusip=None,
        option_type=None,
        putCall=None,
        underlying_symbol=None,
        option_multiplier=None,
        option_deliverables=None,
        **order_leg_kwargs,
    ):
        if instruction not in self.valid_instructions:
            raise Exception(
                f"{instruction} not in valid instruction list for Option Order Leg"
            )

        instrument = OptionInstrument(
            symbol=symbol,
            assetType=self.asset_type,
            description=description,
            cusip=cusip,
            type=option_type,
            putCall=putCall,
            underlyingSymbol=underlying_symbol,
            optionMultiplier=option_multiplier,
            optionDeliverables=option_deliverables,
        )
        super().__init__(
            instruction=instruction,
            quantity=quantity,
            instrument=instrument,
            **order_leg_kwargs,
        )


def create_option_order_leg(
    instruction, quantity, symbol, description=None, cusip=None, **order_leg_kwargs,
):
    """Creates Option OrderLeg
    """
    asset_type = InstrumentAssetType.OPTION

    instrument = OptionInstrument(symbol=symbol, assetType=asset_type)

    return OrderLeg(
        instruction=instruction,
        quantity=quantity,
        instrument=instrument,
        **order_leg_kwargs,
    )
