"""add last few columns to posts table

Revision ID: 91e5539be788
Revises: 6393aa1f7080
Create Date: 2024-11-19 21:00:56.607235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91e5539be788'
down_revision: Union[str, None] = '6393aa1f7080'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts',sa.Column(
    'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
