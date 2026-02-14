"""add content column to posts table

Revision ID: f3b9458ca21c
Revises: 9a6695c6f29a
Create Date: 2026-02-13 16:49:41.030671

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3b9458ca21c'
down_revision: Union[str, Sequence[str], None] = '9a6695c6f29a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', # table name
                  sa.Column('content', sa.String(), nullable=False))
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts',# table name
                   'content')
    
    pass
