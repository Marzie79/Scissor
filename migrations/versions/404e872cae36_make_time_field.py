"""make time field

Revision ID: 404e872cae36
Revises: 
Create Date: 2020-06-19 03:34:06.024216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404e872cae36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_url',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('long_url', sa.Text(), nullable=True),
    sa.Column('short_url', sa.Text(), nullable=True),
    sa.Column('pub_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_url')
    # ### end Alembic commands ###
