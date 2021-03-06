"""Confirmation Table

Revision ID: d81841bbd9e5
Revises: 5ea0dd5775b6
Create Date: 2021-12-10 15:00:33.436853

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd81841bbd9e5'
down_revision = '5ea0dd5775b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('confirmation',
    sa.Column('confirmation_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('confirmed', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('confirmation_id')
    )
    op.drop_column('booking', 'Confirmation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('Confirmation', mysql.TEXT(), nullable=True))
    op.drop_table('confirmation')
    # ### end Alembic commands ###
