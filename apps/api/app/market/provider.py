from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class SectorData:
    name: str
    relative_strength: float
    momentum: float


@dataclass(frozen=True)
class MarketData:
    nifty50: float
    sensex: float
    bank_nifty: float
    india_vix: float
    advance_decline_ratio: float
    sectors: tuple[SectorData, ...]


class MarketDataProvider(ABC):
    @abstractmethod
    async def fetch_market_data(self) -> MarketData:
        """Return a normalized market-wide data snapshot."""


class MockMarketDataProvider(MarketDataProvider):
    async def fetch_market_data(self) -> MarketData:
        return MarketData(
            nifty50=22_450.35,
            sensex=73_840.12,
            bank_nifty=48_210.75,
            india_vix=13.8,
            advance_decline_ratio=1.42,
            sectors=(
                SectorData("Financial Services", 82.5, 4.2),
                SectorData("Information Technology", 76.0, 3.4),
                SectorData("Healthcare", 68.5, 2.1),
                SectorData("Consumer Goods", 61.0, 1.2),
                SectorData("Energy", 55.5, -0.8),
            ),
        )
