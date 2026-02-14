"""add user table

Revision ID: 4953c837573c
Revises: f3b9458ca21c
Create Date: 2026-02-13 17:28:46.751969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4953c837573c'
down_revision: Union[str, Sequence[str], None] = 'f3b9458ca21c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              nullable=False,
                              server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')                   
    )
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    
    pass
