"""create users

Revision ID: 0001
Revises:
Create Date: 2026-08-05 00:00:00 UTC

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("wallet_address", sa.String(length=42), nullable=False),
        sa.Column("referrer_id", sa.Uuid(), nullable=True),
        sa.Column(
            "has_passport",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default="true",
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint(
            "wallet_address = lower(wallet_address)",
            name="ck_users_wallet_address_lowercase",
        ),
        sa.ForeignKeyConstraint(
            ["referrer_id"],
            ["users.id"],
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_users_wallet_address",
        "users",
        ["wallet_address"],
        unique=True,
    )
    op.create_index(
        "ix_users_referrer_id",
        "users",
        ["referrer_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_users_referrer_id", table_name="users")
    op.drop_index("ix_users_wallet_address", table_name="users")
    op.drop_table("users")
