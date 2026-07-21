from pathlib import Path


def test_market_migration_creates_schema_tables_indexes_and_foreign_keys() -> None:
    migration = Path("migrations/versions/20260719_0001_market_intelligence.py").read_text()
    for fragment in ("CREATE SCHEMA IF NOT EXISTS market", "market_snapshot", "sector_strength", "market_regime", "ix_market_snapshot_snapshot_time", "ix_market_snapshot_market_regime", "ForeignKey"):
        assert fragment in migration


def test_legacy_market_upgrade_restores_timestamp_defaults() -> None:
    migration = Path("migrations/versions/20260721_0003_restore_market_timestamp_defaults.py").read_text()

    assert 'down_revision = "20260721_0002"' in migration
    assert "server_default=sa.text(\"now()\")" in migration
