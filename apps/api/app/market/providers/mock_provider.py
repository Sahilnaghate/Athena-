from datetime import datetime, timezone

from app.market.providers.base import MarketDataProvider
from app.market.schemas import MarketRegimeData, MarketSnapshotData, SectorStrengthData


class MockMarketDataProvider(MarketDataProvider):
    """Deterministic provider for development and provider-contract tests."""

    def get_market_snapshot(self) -> MarketSnapshotData:
        return MarketSnapshotData(snapshot_time=datetime(2026, 7, 21, 9, 15, tzinfo=timezone.utc), nifty50=24_625.80, sensex=80_420.15, india_vix=13.80, advance_decline_ratio=1.42, breadth_score=71.0, market_health_score=78.0)

    def get_sector_strength(self) -> tuple[SectorStrengthData, ...]:
        names_and_scores = (("IT", 89.0, 4.2), ("Banking", 86.0, 3.8), ("Auto", 81.0, 3.1), ("FMCG", 77.0, 2.5), ("Pharma", 74.0, 2.1), ("Energy", 70.0, 1.6), ("Realty", 66.0, 1.0), ("Metal", 61.0, 0.4), ("Media", 57.0, -0.5), ("Infrastructure", 54.0, -1.1))
        return tuple(SectorStrengthData(sector_name=name, rank=index, strength_score=strength, momentum_score=momentum) for index, (name, strength, momentum) in enumerate(names_and_scores, start=1))

    def get_market_regime(self) -> MarketRegimeData:
        return MarketRegimeData(regime="BULL", confidence=82.0, reason="Deterministic mock: positive breadth and moderate volatility.")
