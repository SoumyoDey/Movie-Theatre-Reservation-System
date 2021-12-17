"""schedule

Revision ID: b7e26dcb3acb
Revises: 7a4c09d987fa
Create Date: 2021-11-24 13:47:31.111735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7e26dcb3acb'
down_revision = '7a4c09d987fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('schedule_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'booking', 'schedule', ['schedule_id'], ['schedule_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'booking', type_='foreignkey')
    op.drop_column('booking', 'schedule_id')
    # ### end Alembic commands ###