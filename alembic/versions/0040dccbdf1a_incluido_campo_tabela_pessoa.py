"""incluido campo tabela Pessoa

Revision ID: 0040dccbdf1a
Revises: 6d32e1ccf3c2
Create Date: 2024-01-29 23:49:06.956578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0040dccbdf1a'
down_revision: Union[str, None] = '6d32e1ccf3c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
