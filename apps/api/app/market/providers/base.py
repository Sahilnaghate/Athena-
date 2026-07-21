from abc import ABC, abstractmethod

from app.market.schemas import MarketRegimeData, MarketSnapshotData, SectorStrengthData


class MarketDataProvider(ABC):
    """Provider contract that future Market services depend upon."""

    @abstractmethod
    def get_market_snapshot(self) -> MarketSnapshotData:
        """Return a normalized market snapshot."""

    @abstractmethod
    def get_sector_strength(self) -> tuple[SectorStrengthData, ...]:
        """Return the current sector strength ranking."""

    @abstractmethod
    def get_market_regime(self) -> MarketRegimeData:
        """Return the current market regime observation."""
