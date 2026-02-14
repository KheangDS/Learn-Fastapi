"""add last few columns to posts table

Revision ID: 81b214d439a4
Revises: c4a0fb923fdf
Create Date: 2026-02-14 00:42:39.077934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81b214d439a4'
down_revision: Union[str, Sequence[str], None] = 'c4a0fb923fdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', # table name
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', # table name
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', # table name
                   'published' # column name
    )
    op.drop_column('posts', # table name
                   'created_at' # column name
    )
    pass
