from typing import List
from dataclasses import dataclass
from .base import BaseOrder
from .constants import (
    InstrumentAssetType,
    MutualFundType,
    CashEquivalentType,
    OptionType,
    OptionDeliverableCurrencyType,
    OptionPutCall,
)


@dataclass
class Instrument(BaseOrder):
    """Base Instrument class
    """

    pass


@dataclass
class Equity(Instrument):
    """Equity Instrument
    """

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None


@dataclass
class FixedIncome(Instrument):
    """Fixed Income Instrument
    """

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    maturityDate: str = None
    variableRate: int = None
    factor: int = None


@dataclass
class MutualFund(Instrument):
    """Mutual Fund Instrument
    """

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    type: MutualFundType = None


@dataclass
class CashEquivalent(Instrument):
    """Cash Equivalent Instrument
    """

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
class Option(Instrument):
    """Option Instrument
    """

    assetType: InstrumentAssetType = None
    cusip: str = None
    symbol: str = None
    description: str = None
    type: OptionType = None
    putCall: OptionPutCall = None
    underlyingSymbol: str = None
    optionMultiplier: int = None
    optionDeliverables: List[OptionDeliverable] = None
