"""add foreign-key to posts table

Revision ID: c4a0fb923fdf
Revises: 4953c837573c
Create Date: 2026-02-14 00:11:50.431100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4a0fb923fdf'
down_revision: Union[str, Sequence[str], None] = '4953c837573c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', # table name
                  sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', # constraint name
                          source_table='posts', # source table name
                          referent_table='users', # referent table name
                          local_cols=['owner_id'], # source column names
                          remote_cols=['id'], # referent column names
                          ondelete='CASCADE' # on delete behavior
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_users_fk', # constraint name
                       table_name='posts' # table name
    )
    op.drop_column('posts', # table name
                   'owner_id' # column name
    )
    pass
