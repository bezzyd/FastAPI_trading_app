"""Initial

Revision ID: 3920c1fe80bf
Revises: 
Create Date: 2023-06-02 20:57:57.804363

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3920c1fe80bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('is_superuser', sa.Boolean(), nullable=True),
                    sa.Column('is_verified', sa.Boolean(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='users_role_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='users_pkey')
                    )
    op.create_table('roles',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('permissions', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='roles_pkey')
                    )
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
