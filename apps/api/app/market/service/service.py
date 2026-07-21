import logging

from app.market.models import MarketRegime, MarketSnapshot, SectorStrength
from app.market.providers import MarketDataProvider
from app.market.repository import MarketRepository


class MarketProviderError(RuntimeError):
    """Raised when a Market provider cannot supply valid data."""


class MarketPersistenceError(RuntimeError):
    """Raised when a Market data refresh cannot be persisted."""


class MarketService:
    """Coordinates provider data and the Market persistence boundary."""

    def __init__(self, provider: MarketDataProvider, repository: MarketRepository, logger: logging.Logger):
        self._provider = provider
        self._repository = repository
        self._logger = logger

    def refresh_market(self) -> MarketSnapshot:
        """Retrieve provider data and persist one complete Market observation."""
        self._logger.info("Market refresh started", extra={"service": "market"})
        try:
            snapshot_data = self._provider.get_market_snapshot()
            sectors = self._provider.get_sector_strength()
            regime = self._provider.get_market_regime()
        except Exception as error:
            self._logger.exception("Market provider failed", extra={"service": "market"})
            raise MarketProviderError("Market provider could not supply data") from error

        try:
            snapshot = self._repository.create_snapshot(MarketSnapshot(snapshot_time=snapshot_data.snapshot_time, market_status="OPEN", market_regime=regime.regime, market_health_score=snapshot_data.market_health_score, advance_decline_ratio=snapshot_data.advance_decline_ratio, volatility_index=snapshot_data.india_vix, breadth_score=snapshot_data.breadth_score))
            for sector in sectors:
                self._repository.create_sector_strength(SectorStrength(snapshot_id=snapshot.id, sector_name=sector.sector_name, rank=sector.rank, strength_score=sector.strength_score, momentum_score=sector.momentum_score))
            self._repository.create_market_regime(MarketRegime(snapshot_id=snapshot.id, regime=regime.regime, confidence=regime.confidence, reason=regime.reason))
            self._repository.commit()
        except Exception as error:
            self._repository.rollback()
            self._logger.exception("Market persistence failed", extra={"service": "market"})
            raise MarketPersistenceError("Market data could not be persisted") from error

        self._logger.info("Market persistence completed", extra={"service": "market", "snapshot_id": str(snapshot.id)})
        self._logger.info("Market refresh completed", extra={"service": "market", "snapshot_id": str(snapshot.id)})
        return self._repository.get_latest_snapshot() or snapshot

    def get_latest_market(self) -> MarketSnapshot | None:
        """Return the latest persisted Market snapshot."""
        return self._repository.get_latest_snapshot()

    def list_market_history(self) -> list[MarketSnapshot]:
        """Return persisted Market snapshots in repository-defined order."""
        return self._repository.list_snapshots()

    def get_snapshot_regime(self, snapshot: MarketSnapshot) -> MarketRegime | None:
        """Return the persisted regime associated with one Market snapshot."""
        return self._repository.get_market_regime(snapshot.id)

    def get_latest_market_state(self) -> tuple[MarketSnapshot, MarketRegime | None, list[SectorStrength]] | None:
        """Return the latest snapshot with its persisted regime and sector strengths."""
        snapshot = self._repository.get_latest_snapshot()
        if snapshot is None:
            return None
        return snapshot, self._repository.get_market_regime(snapshot.id), self._repository.get_sector_strength(snapshot.id)
