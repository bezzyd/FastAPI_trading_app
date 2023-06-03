"""solve column problem

Revision ID: 32ac64b88588
Revises: 91ca14827e20
Create Date: 2023-06-03 15:59:52.780034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ac64b88588'
down_revision = '91ca14827e20'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation', sa.Column('quantity', sa.String(), nullable=True))
    op.drop_column('operation', 'quanity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation', sa.Column('quanity', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('operation', 'quantity')
    # ### end Alembic commands ###