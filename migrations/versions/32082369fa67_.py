"""empty message

Revision ID: 32082369fa67
Revises: None
Create Date: 2017-03-10 22:57:03.510904

"""

# revision identifiers, used by Alembic.
revision = '32082369fa67'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('modified', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('app_board')
    ### end Alembic commands ###