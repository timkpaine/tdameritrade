from dataclasses import dataclass
from typing import List

from ..constants import (
    CashEquivalentType,
    InstrumentAssetType,
    MutualFundType,
    OptionDeliverableCurrencyType,
    OptionPutCall,
    OptionType,
)
from .base import BaseOrder


@dataclass
class Instrument(BaseOrder):
    """Base Instrument class"""

    pass


@dataclass
class EquityInstrument(Instrument):
    """Equity Instrument"""

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None


@dataclass
class FixedIncomeInstrument(Instrument):
    """Fixed Income Instrument"""

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    maturityDate: str = None
    variableRate: int = None
    factor: int = None


@dataclass
class MutualFundInstrument(Instrument):
    """Mutual Fund Instrument"""

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    type: MutualFundType = None


@dataclass
class CashEquivalentInstrument(Instrument):
    """Cash Equivalent Instrument"""

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    type: CashEquivalentType = None


@dataclass
class OptionDeliverable(BaseOrder):
    """Option Deliverable in Option's optionDeliverables list

    This class is not an instrument itself
    """

    symbol: str = None
    deliverableUnits: int = None
    currencyType: OptionDeliverableCurrencyType = None
    assetType: InstrumentAssetType = None


@dataclass
class OptionInstrument(Instrument):
    """Option Instrument"""

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    type: OptionType = None
    putCall: OptionPutCall = None
    underlyingSymbol: str = None
    optionMultiplier: int = None
    optionDeliverables: List = (
        None  # List[OptionDeliverable]. Issue with List[type] formatting
    )
