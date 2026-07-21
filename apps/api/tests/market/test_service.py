from datetime import datetime, timezone
from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from app.market.models import MarketSnapshot
from app.market.providers import MockMarketDataProvider
from app.market.repository import MarketRepository
from app.market.service import MarketPersistenceError, MarketProviderError, MarketService


def build_service() -> tuple[MarketService, MagicMock, MagicMock]:
    provider = MagicMock(spec=MockMarketDataProvider)
    provider.get_market_snapshot.return_value = MockMarketDataProvider().get_market_snapshot()
    provider.get_sector_strength.return_value = MockMarketDataProvider().get_sector_strength()
    provider.get_market_regime.return_value = MockMarketDataProvider().get_market_regime()
    repository = MagicMock(spec=MarketRepository)
    snapshot = MarketSnapshot(id=uuid4(), snapshot_time=datetime.now(timezone.utc), market_status="OPEN", market_regime="BULL", market_health_score=78, advance_decline_ratio=1.4, volatility_index=14, breadth_score=70)
    repository.create_snapshot.return_value = snapshot
    repository.get_latest_snapshot.return_value = snapshot
    return MarketService(provider, repository, MagicMock()), provider, repository


def test_refresh_market_persists_provider_data() -> None:
    service, provider, repository = build_service()
    snapshot = service.refresh_market()
    assert snapshot is repository.get_latest_snapshot.return_value
    provider.get_market_snapshot.assert_called_once()
    assert repository.create_sector_strength.call_count == 10
    repository.create_market_regime.assert_called_once()
    repository.commit.assert_called_once()


def test_get_latest_market_delegates_to_repository() -> None:
    service, _, repository = build_service()
    assert service.get_latest_market() is repository.get_latest_snapshot.return_value


def test_list_market_history_delegates_to_repository() -> None:
    service, _, repository = build_service()
    repository.list_snapshots.return_value = []
    assert service.list_market_history() == []


def test_refresh_market_wraps_provider_failures() -> None:
    service, provider, _ = build_service()
    provider.get_market_snapshot.side_effect = ValueError("invalid")
    with pytest.raises(MarketProviderError):
        service.refresh_market()


def test_refresh_market_rolls_back_persistence_failures() -> None:
    service, _, repository = build_service()
    repository.create_snapshot.side_effect = RuntimeError("database unavailable")
    with pytest.raises(MarketPersistenceError):
        service.refresh_market()
    repository.rollback.assert_called_once()
