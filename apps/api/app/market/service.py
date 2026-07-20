from datetime import datetime

from app.market.calculators import MarketHealthCalculator, MarketRegimeDetector
from app.market.provider import MarketDataProvider
from app.market.repository import MarketRepository


class MarketService:
    def __init__(self, repository: MarketRepository, provider: MarketDataProvider, calculator: MarketHealthCalculator, detector: MarketRegimeDetector):
        self._repository = repository
        self._provider = provider
        self._calculator = calculator
        self._detector = detector

    async def refresh(self) -> dict:
        data = await self._provider.fetch_market_data()
        health_score = self._calculator.calculate(data)
        regime = self._detector.detect(data, health_score)
        snapshot = self._repository.store_snapshot(data, regime, health_score)
        return self.overview(snapshot.captured_at)

    def overview(self, updated_at: datetime | None = None) -> dict:
        snapshot = self._repository.latest_snapshot()
        regime = self._repository.latest_regime()
        if snapshot is None or regime is None:
            return {"market_health": None, "market_regime": None, "last_updated": None, "sectors": []}
        sectors = self._repository.sector_ranking(snapshot.id)
        return {"market_health": float(regime.health_score), "market_regime": regime.regime, "last_updated": updated_at or snapshot.captured_at, "sectors": [{"name": item.sector_name, "rank": item.rank, "relative_strength": float(item.relative_strength), "momentum": float(item.momentum), "trend": item.trend} for item in sectors]}

    def regime(self) -> dict:
        regime = self._repository.latest_regime()
        return {"market_regime": regime.regime if regime else None, "market_health": float(regime.health_score) if regime else None, "last_updated": regime.detected_at if regime else None}

    def sectors(self) -> list[dict]:
        snapshot = self._repository.latest_snapshot()
        return [] if snapshot is None else self.overview()["sectors"]
