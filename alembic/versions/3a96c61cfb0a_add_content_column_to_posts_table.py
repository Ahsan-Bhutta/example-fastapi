"""add content column to posts table

Revision ID: 3a96c61cfb0a
Revises: 27325d82a740
Create Date: 2024-11-19 20:05:44.598128

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a96c61cfb0a'
down_revision: Union[str, None] = '27325d82a740'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
