"""upgrade the pre-M2 Market schema to the M2 schema

Revision ID: 20260721_0002
Revises: 20260719_0001
Create Date: 2026-07-21

The initial Market migration was applied during the platform bootstrap with
an earlier table shape.  This migration preserves any development records
while bringing databases already stamped at the original revision in line
with the finalized M2 schema.
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "20260721_0002"
down_revision = "20260719_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if not inspector.has_table("market_snapshot", schema="market"):
        return

    snapshot_columns = {column["name"] for column in inspector.get_columns("market_snapshot", schema="market")}
    # ``captured_at`` is exclusive to the pre-M2 bootstrap schema.  A clean
    # install has the canonical ``snapshot_time`` column from revision 0001.
    if "captured_at" not in snapshot_columns:
        return

    def add_column_if_missing(table_name: str, column: sa.Column[object]) -> None:
        columns = {item["name"] for item in sa.inspect(op.get_bind()).get_columns(table_name, schema="market")}
        if column.name not in columns:
            op.add_column(table_name, column, schema="market")

    def drop_column_if_present(table_name: str, column_name: str) -> None:
        columns = {item["name"] for item in sa.inspect(op.get_bind()).get_columns(table_name, schema="market")}
        if column_name in columns:
            op.drop_column(table_name, column_name, schema="market")

    def create_index_if_missing(index_name: str, table_name: str, columns: list[str]) -> None:
        indexes = {index["name"] for index in sa.inspect(op.get_bind()).get_indexes(table_name, schema="market")}
        if index_name not in indexes:
            op.create_index(index_name, table_name, columns, schema="market")

    add_column_if_missing("market_snapshot", sa.Column("snapshot_time", sa.DateTime(timezone=True), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("market_status", sa.String(20), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("market_regime", sa.String(20), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("market_health_score", sa.Numeric(5, 2), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("volatility_index", sa.Numeric(8, 2), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("breadth_score", sa.Numeric(8, 2), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("created_at", sa.DateTime(timezone=True), nullable=True))
    add_column_if_missing("market_snapshot", sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True))
    op.execute(
        """
        UPDATE market.market_snapshot AS snapshot
        SET snapshot_time = snapshot.captured_at,
            market_status = 'OPEN',
            market_regime = COALESCE(regime.regime, 'SIDEWAYS'),
            market_health_score = COALESCE(regime.health_score, 50),
            volatility_index = COALESCE(snapshot.india_vix, 0),
            breadth_score = COALESCE(regime.health_score, 50),
            created_at = snapshot.captured_at,
            updated_at = snapshot.captured_at
        FROM market.market_regime AS regime
        WHERE snapshot.regime_id = regime.id
        """
    )
    op.execute(
        """
        UPDATE market.market_snapshot
        SET snapshot_time = COALESCE(snapshot_time, now()),
            market_status = COALESCE(market_status, 'OPEN'),
            market_regime = COALESCE(market_regime, 'SIDEWAYS'),
            market_health_score = COALESCE(market_health_score, 50),
            volatility_index = COALESCE(volatility_index, 0),
            breadth_score = COALESCE(breadth_score, 50),
            created_at = COALESCE(created_at, now()),
            updated_at = COALESCE(updated_at, now())
        """
    )
    for column_name in ("snapshot_time", "market_status", "market_regime", "market_health_score", "volatility_index", "breadth_score", "created_at", "updated_at"):
        op.alter_column("market_snapshot", column_name, nullable=False, schema="market")
    for column_name in ("nifty50", "sensex", "bank_nifty", "india_vix", "captured_at"):
        drop_column_if_present("market_snapshot", column_name)
    create_index_if_missing("ix_market_snapshot_snapshot_time", "market_snapshot", ["snapshot_time"])
    create_index_if_missing("ix_market_snapshot_market_regime", "market_snapshot", ["market_regime"])

    add_column_if_missing("sector_strength", sa.Column("strength_score", sa.Numeric(8, 2), nullable=True))
    add_column_if_missing("sector_strength", sa.Column("momentum_score", sa.Numeric(8, 2), nullable=True))
    add_column_if_missing("sector_strength", sa.Column("created_at", sa.DateTime(timezone=True), nullable=True))
    op.execute("UPDATE market.sector_strength SET strength_score = relative_strength, momentum_score = momentum, created_at = now()")
    for column_name in ("strength_score", "momentum_score", "created_at"):
        op.alter_column("sector_strength", column_name, nullable=False, schema="market")
    for column_name in ("relative_strength", "momentum", "trend"):
        drop_column_if_present("sector_strength", column_name)

    add_column_if_missing("market_regime", sa.Column("snapshot_id", postgresql.UUID(as_uuid=True), nullable=True))
    add_column_if_missing("market_regime", sa.Column("confidence", sa.Numeric(5, 2), nullable=True))
    add_column_if_missing("market_regime", sa.Column("reason", sa.String(500), nullable=True))
    add_column_if_missing("market_regime", sa.Column("created_at", sa.DateTime(timezone=True), nullable=True))
    op.execute(
        """
        UPDATE market.market_regime AS regime
        SET snapshot_id = snapshot.id,
            confidence = LEAST(GREATEST(COALESCE(regime.health_score, 50), 0), 100),
            reason = 'Migrated from the platform bootstrap Market schema.',
            created_at = COALESCE(regime.detected_at, now())
        FROM market.market_snapshot AS snapshot
        WHERE snapshot.regime_id = regime.id
        """
    )
    op.execute("DELETE FROM market.market_regime WHERE snapshot_id IS NULL")
    for column_name in ("snapshot_id", "confidence", "reason", "created_at"):
        op.alter_column("market_regime", column_name, nullable=False, schema="market")
    foreign_keys = {key["name"] for key in sa.inspect(op.get_bind()).get_foreign_keys("market_regime", schema="market")}
    if "fk_market_regime_snapshot_id" not in foreign_keys:
        op.create_foreign_key("fk_market_regime_snapshot_id", "market_regime", "market_snapshot", ["snapshot_id"], ["id"], source_schema="market", referent_schema="market")
    drop_column_if_present("market_regime", "health_score")
    drop_column_if_present("market_regime", "detected_at")
    drop_column_if_present("market_snapshot", "regime_id")


def downgrade() -> None:
    op.add_column("market_regime", sa.Column("health_score", sa.Numeric(5, 2), nullable=True), schema="market")
    op.add_column("market_regime", sa.Column("detected_at", sa.DateTime(timezone=True), nullable=True), schema="market")
    op.execute("UPDATE market.market_regime SET health_score = confidence, detected_at = created_at")

    op.add_column("market_snapshot", sa.Column("regime_id", postgresql.UUID(as_uuid=True), nullable=True), schema="market")
    op.add_column("market_snapshot", sa.Column("nifty50", sa.Numeric(12, 2), nullable=True), schema="market")
    op.add_column("market_snapshot", sa.Column("sensex", sa.Numeric(12, 2), nullable=True), schema="market")
    op.add_column("market_snapshot", sa.Column("bank_nifty", sa.Numeric(12, 2), nullable=True), schema="market")
    op.add_column("market_snapshot", sa.Column("india_vix", sa.Numeric(8, 2), nullable=True), schema="market")
    op.add_column("market_snapshot", sa.Column("captured_at", sa.DateTime(timezone=True), nullable=True), schema="market")
    op.execute(
        """
        UPDATE market.market_snapshot AS snapshot
        SET regime_id = (
                SELECT regime.id FROM market.market_regime AS regime
                WHERE regime.snapshot_id = snapshot.id
                ORDER BY regime.created_at DESC LIMIT 1
            ),
            nifty50 = 0,
            sensex = 0,
            bank_nifty = 0,
            india_vix = volatility_index,
            captured_at = snapshot_time
        """
    )
    op.drop_index("ix_market_snapshot_market_regime", table_name="market_snapshot", schema="market")
    op.drop_index("ix_market_snapshot_snapshot_time", table_name="market_snapshot", schema="market")
    for column_name in ("snapshot_time", "market_status", "market_regime", "market_health_score", "volatility_index", "breadth_score", "created_at", "updated_at"):
        op.drop_column("market_snapshot", column_name, schema="market")

    op.add_column("sector_strength", sa.Column("relative_strength", sa.Numeric(8, 2), nullable=True), schema="market")
    op.add_column("sector_strength", sa.Column("momentum", sa.Numeric(8, 2), nullable=True), schema="market")
    op.add_column("sector_strength", sa.Column("trend", sa.String(20), nullable=True), schema="market")
    op.execute("UPDATE market.sector_strength SET relative_strength = strength_score, momentum = momentum_score, trend = 'NEUTRAL'")
    for column_name in ("strength_score", "momentum_score", "created_at"):
        op.drop_column("sector_strength", column_name, schema="market")

    op.drop_constraint("fk_market_regime_snapshot_id", "market_regime", schema="market", type_="foreignkey")
    for column_name in ("snapshot_id", "confidence", "reason", "created_at"):
        op.drop_column("market_regime", column_name, schema="market")
