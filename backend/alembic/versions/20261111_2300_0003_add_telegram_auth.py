"""add telegram auth

Revision ID: 0003
Revises: 0002
Create Date: 2026-11-11 23:00:00 UTC

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0003"
down_revision: str | None = "0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "wallet_address",
        existing_type=sa.String(length=42),
        nullable=True,
    )
    op.add_column("users", sa.Column("telegram_id", sa.BigInteger(), nullable=True))
    op.add_column(
        "users",
        sa.Column("telegram_username", sa.String(length=32), nullable=True),
    )
    op.add_column("users", sa.Column("first_name", sa.String(length=64), nullable=True))
    op.add_column(
        "users",
        sa.Column("avatar_url", sa.String(length=2048), nullable=True),
    )
    op.create_index(
        "ix_users_telegram_id",
        "users",
        ["telegram_id"],
        unique=True,
    )
    op.drop_constraint(
        "ck_users_wallet_address_lowercase",
        "users",
        type_="check",
    )
    op.create_check_constraint(
        "ck_users_wallet_address_lowercase",
        "users",
        "wallet_address IS NULL OR wallet_address = lower(wallet_address)",
    )
    op.create_check_constraint(
        "ck_users_identity",
        "users",
        "wallet_address IS NOT NULL OR telegram_id IS NOT NULL",
    )


def downgrade() -> None:
    connection = op.get_bind()
    telegram_only_users = connection.scalar(
        sa.select(sa.func.count())
        .select_from(sa.table("users", sa.column("wallet_address")))
        .where(sa.column("wallet_address").is_(None))
    )
    if telegram_only_users:
        raise RuntimeError(
            "Cannot downgrade while Telegram-only users exist; "
            "link their wallets or migrate them explicitly first"
        )
    op.drop_constraint("ck_users_identity", "users", type_="check")
    op.drop_constraint(
        "ck_users_wallet_address_lowercase",
        "users",
        type_="check",
    )
    op.create_check_constraint(
        "ck_users_wallet_address_lowercase",
        "users",
        "wallet_address = lower(wallet_address)",
    )
    op.drop_index("ix_users_telegram_id", table_name="users")
    op.drop_column("users", "avatar_url")
    op.drop_column("users", "first_name")
    op.drop_column("users", "telegram_username")
    op.drop_column("users", "telegram_id")
    op.alter_column(
        "users",
        "wallet_address",
        existing_type=sa.String(length=42),
        nullable=True,
    )
    op.alter_column(
        "users",
        "wallet_address",
        existing_type=sa.String(length=42),
        nullable=False,
    )
