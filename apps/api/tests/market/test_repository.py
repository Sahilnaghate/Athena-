from datetime import datetime, timezone
from unittest.mock import MagicMock

from app.market.models import MarketRegime, MarketSnapshot, SectorStrength
from app.market.repository import MarketRepository


def test_create_snapshot_adds_and_flushes_record() -> None:
    session = MagicMock()
    snapshot = MarketSnapshot(snapshot_time=datetime.now(timezone.utc), market_status="OPEN", market_regime="BULL", market_health_score=75, advance_decline_ratio=1.2, volatility_index=14, breadth_score=70)
    assert MarketRepository(session).create_snapshot(snapshot) is snapshot
    session.add.assert_called_once_with(snapshot)
    session.flush.assert_called_once()


def test_get_latest_snapshot_uses_descending_snapshot_time() -> None:
    session = MagicMock()
    expected = MagicMock()
    session.scalar.return_value = expected
    assert MarketRepository(session).get_latest_snapshot() is expected
    session.scalar.assert_called_once()


def test_list_snapshots_returns_records() -> None:
    session = MagicMock()
    snapshots = [MagicMock(), MagicMock()]
    session.scalars.return_value = snapshots
    assert MarketRepository(session).list_snapshots() == snapshots


def test_create_sector_strength_adds_and_flushes_record() -> None:
    session = MagicMock()
    sector = MagicMock(spec=SectorStrength)
    assert MarketRepository(session).create_sector_strength(sector) is sector
    session.add.assert_called_once_with(sector)
    session.flush.assert_called_once()


def test_get_sector_strength_returns_ranked_records() -> None:
    session = MagicMock()
    sectors = [MagicMock(), MagicMock()]
    session.scalars.return_value = sectors
    assert MarketRepository(session).get_sector_strength(MagicMock()) == sectors


def test_create_market_regime_adds_and_flushes_record() -> None:
    session = MagicMock()
    regime = MagicMock(spec=MarketRegime)
    assert MarketRepository(session).create_market_regime(regime) is regime
    session.add.assert_called_once_with(regime)
    session.flush.assert_called_once()


def test_get_market_regime_returns_latest_record() -> None:
    session = MagicMock()
    regime = MagicMock()
    session.scalar.return_value = regime
    assert MarketRepository(session).get_market_regime(MagicMock()) is regime
