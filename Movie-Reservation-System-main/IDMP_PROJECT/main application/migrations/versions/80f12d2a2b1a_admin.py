"""admin

Revision ID: 80f12d2a2b1a
Revises: f39ec4b910ea
Create Date: 2021-11-24 16:02:57.061653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80f12d2a2b1a'
down_revision = 'f39ec4b910ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('admin_email', sa.String(length=64), nullable=True),
    sa.Column('admin_pass', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_index(op.f('ix_admin_admin_email'), 'admin', ['admin_email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_admin_admin_email'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
