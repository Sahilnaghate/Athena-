from app.market.models import MarketRegime, MarketSnapshot, SectorStrength


def test_market_schema_models_define_expected_tables() -> None:
    assert MarketSnapshot.__table__.schema == "market"
    assert SectorStrength.__table__.foreign_keys
    assert MarketRegime.__table__.foreign_keys
    assert {index.name for index in MarketSnapshot.__table__.indexes} == {
        "ix_market_snapshot_market_regime",
        "ix_market_snapshot_snapshot_time",
    }
