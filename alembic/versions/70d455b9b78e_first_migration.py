"""First migration

Revision ID: 70d455b9b78e
Revises: 
Create Date: 2023-02-25 00:13:22.254379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70d455b9b78e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('counteragents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('full_name', sa.String(length=150), nullable=True),
    sa.Column('inn', sa.Integer(), nullable=False),
    sa.Column('kpp', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('counteragents')
    # ### end Alembic commands ###
