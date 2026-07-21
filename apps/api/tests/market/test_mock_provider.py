import pytest
from pydantic import ValidationError

from app.market.providers import MarketDataProvider, MockMarketDataProvider
from app.market.schemas import MarketSnapshotData


def test_mock_provider_implements_contract() -> None:
    assert isinstance(MockMarketDataProvider(), MarketDataProvider)


def test_mock_provider_returns_deterministic_snapshot() -> None:
    provider = MockMarketDataProvider()
    assert provider.get_market_snapshot() == provider.get_market_snapshot()
    assert provider.get_market_snapshot().market_health_score == 78.0


def test_mock_provider_returns_ten_ranked_sectors() -> None:
    sectors = MockMarketDataProvider().get_sector_strength()
    assert len(sectors) == 10
    assert [sector.rank for sector in sectors] == list(range(1, 11))


def test_mock_provider_returns_valid_bull_regime() -> None:
    regime = MockMarketDataProvider().get_market_regime()
    assert regime.regime == "BULL"
    assert 0 <= regime.confidence <= 100


def test_snapshot_dto_rejects_invalid_health_score() -> None:
    with pytest.raises(ValidationError):
        MarketSnapshotData(snapshot_time=MockMarketDataProvider().get_market_snapshot().snapshot_time, nifty50=1, sensex=1, india_vix=1, advance_decline_ratio=1, market_health_score=101)
