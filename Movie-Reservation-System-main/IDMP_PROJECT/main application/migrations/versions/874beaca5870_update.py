""" Update

Revision ID: 874beaca5870
Revises: 80f12d2a2b1a
Create Date: 2021-11-26 12:26:01.966512

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '874beaca5870'
down_revision = '80f12d2a2b1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_admin_admin_email', table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('admin_email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('admin_pass', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('admin_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_admin_admin_email', 'admin', ['admin_email'], unique=True)
    # ### end Alembic commands ###
