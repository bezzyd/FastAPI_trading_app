"""Add Operation

Revision ID: 91ca14827e20
Revises: 3920c1fe80bf
Create Date: 2023-06-03 14:59:36.834397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91ca14827e20'
down_revision = '3920c1fe80bf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('quanity', sa.String(), nullable=True),
                    sa.Column('figi', sa.String(), nullable=True),
                    sa.Column('instrument_type', sa.String(), nullable=True),
                    sa.Column('data', sa.TIMESTAMP(), nullable=True),
                    sa.Column('type', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.alter_column('user', 'is_active',
                    existing_type=sa.BOOLEAN(),
                    nullable=False)
    op.alter_column('user', 'is_superuser',
                    existing_type=sa.BOOLEAN(),
                    nullable=False)
    op.alter_column('user', 'is_verified',
                    existing_type=sa.BOOLEAN(),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_verified',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    op.alter_column('user', 'is_superuser',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    op.alter_column('user', 'is_active',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    op.drop_table('operation')
    # ### end Alembic commands ###