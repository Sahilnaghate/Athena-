"""create market intelligence schema

Revision ID: 20260719_0001
Revises:
Create Date: 2026-07-19
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20260719_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS market")
    op.create_table("market_snapshot", sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True), sa.Column("snapshot_time", sa.DateTime(timezone=True), nullable=False), sa.Column("market_status", sa.String(20), nullable=False), sa.Column("market_regime", sa.String(20), nullable=False), sa.Column("market_health_score", sa.Numeric(5, 2), nullable=False), sa.Column("advance_decline_ratio", sa.Numeric(8, 2), nullable=False), sa.Column("volatility_index", sa.Numeric(8, 2), nullable=False), sa.Column("breadth_score", sa.Numeric(8, 2), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), schema="market")
    op.create_index("ix_market_snapshot_snapshot_time", "market_snapshot", ["snapshot_time"], schema="market")
    op.create_index("ix_market_snapshot_market_regime", "market_snapshot", ["market_regime"], schema="market")
    op.create_table("sector_strength", sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True), sa.Column("snapshot_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("market.market_snapshot.id"), nullable=False), sa.Column("sector_name", sa.String(100), nullable=False), sa.Column("rank", sa.Integer, nullable=False), sa.Column("strength_score", sa.Numeric(8, 2), nullable=False), sa.Column("momentum_score", sa.Numeric(8, 2), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), schema="market")
    op.create_table("market_regime", sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True), sa.Column("snapshot_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("market.market_snapshot.id"), nullable=False), sa.Column("regime", sa.String(20), nullable=False), sa.Column("confidence", sa.Numeric(5, 2), nullable=False), sa.Column("reason", sa.String(500), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), schema="market")


def downgrade() -> None:
    op.drop_table("market_regime", schema="market")
    op.drop_table("sector_strength", schema="market")
    op.drop_index("ix_market_snapshot_market_regime", table_name="market_snapshot", schema="market")
    op.drop_index("ix_market_snapshot_snapshot_time", table_name="market_snapshot", schema="market")
    op.drop_table("market_snapshot", schema="market")
    op.execute("DROP SCHEMA market")
