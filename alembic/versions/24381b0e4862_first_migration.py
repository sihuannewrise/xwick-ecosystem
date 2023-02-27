"""First migration

Revision ID: 24381b0e4862
Revises: 
Create Date: 2023-02-28 00:25:33.226279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24381b0e4862'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('bic', sa.Integer(), nullable=False),
    sa.Column('correspondent_account', sa.String(length=20), nullable=True),
    sa.Column('payment_city', sa.String(length=150), nullable=False),
    sa.Column('swift', sa.String(length=11), nullable=True),
    sa.Column('registration_number', sa.Integer(), nullable=True),
    sa.Column('treasury_accounts', sa.String(length=20), nullable=True),
    sa.Column('opf_type', sa.String(length=50), nullable=True),
    sa.Column('inn', sa.Integer(), nullable=True),
    sa.Column('kpp', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('actuality_date', sa.DateTime(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('liquidation_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bic'),
    sa.UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),
    sa.UniqueConstraint('name')
    )
    op.create_table('counteragents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('inn', sa.Integer(), nullable=True),
    sa.Column('kpp', sa.Integer(), nullable=True),
    sa.Column('ogrn', sa.String(length=20), nullable=True),
    sa.Column('ogrn_date', sa.DateTime(), nullable=True),
    sa.Column('counteragent_type', sa.String(length=50), nullable=True),
    sa.Column('opf_short', sa.String(length=10), nullable=True),
    sa.Column('name_short_with_opf', sa.String(length=150), nullable=True),
    sa.Column('ip_surname', sa.String(length=100), nullable=True),
    sa.Column('ip_name', sa.String(length=100), nullable=True),
    sa.Column('ip_patronymic', sa.String(length=100), nullable=True),
    sa.Column('management_name', sa.String(length=300), nullable=True),
    sa.Column('management_post', sa.String(length=100), nullable=True),
    sa.Column('address_full_with_index', sa.String(length=300), nullable=True),
    sa.Column('address_egrul', sa.String(length=300), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('actuality_date', sa.DateTime(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('liquidation_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('counteragents')
    op.drop_table('banks')
    # ### end Alembic commands ###
