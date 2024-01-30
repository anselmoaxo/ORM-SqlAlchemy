"""create table pedido

Revision ID: 6d32e1ccf3c2
Revises: 
Create Date: 2024-01-29 23:39:58.184466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d32e1ccf3c2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pedido',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('numero_pedido', sa.Integer(), nullable=False),
        sa.Column('descricao_pedido', sa.String(200)),
    )


def downgrade() -> None:
    pass
