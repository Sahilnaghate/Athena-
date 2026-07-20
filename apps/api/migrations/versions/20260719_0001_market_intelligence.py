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
    op.create_table("market_regime", sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True), sa.Column("regime", sa.String(20), nullable=False), sa.Column("health_score", sa.Numeric(5, 2), nullable=False), sa.Column("detected_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), schema="market")
    op.create_table("market_snapshot", sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True), sa.Column("regime_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("market.market_regime.id"), nullable=False), sa.Column("nifty50", sa.Numeric(12, 2), nullable=False), sa.Column("sensex", sa.Numeric(12, 2), nullable=False), sa.Column("bank_nifty", sa.Numeric(12, 2), nullable=False), sa.Column("india_vix", sa.Numeric(8, 2), nullable=False), sa.Column("advance_decline_ratio", sa.Numeric(8, 2), nullable=False), sa.Column("captured_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), schema="market")
    op.create_table("sector_strength", sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True), sa.Column("snapshot_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("market.market_snapshot.id"), nullable=False), sa.Column("sector_name", sa.String(100), nullable=False), sa.Column("rank", sa.Integer, nullable=False), sa.Column("relative_strength", sa.Numeric(8, 2), nullable=False), sa.Column("momentum", sa.Numeric(8, 2), nullable=False), sa.Column("trend", sa.String(20), nullable=False), schema="market")


def downgrade() -> None:
    op.drop_table("sector_strength", schema="market")
    op.drop_table("market_snapshot", schema="market")
    op.drop_table("market_regime", schema="market")
    op.execute("DROP SCHEMA market")
