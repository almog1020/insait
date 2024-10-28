"""Add question time column

Revision ID: 372c84b07b05
Revises: 
Create Date: 2024-10-22 19:29:59.019433

"""
from math import trunc
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '372c84b07b05'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'questions',
        sa.Column('question_time', sa.DateTime(timezone=True), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('questions','question_time')
