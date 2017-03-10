"""empty message

Revision ID: 2b3e9410ac43
Revises: None
Create Date: 2017-03-10 21:45:33.163059

"""

# revision identifiers, used by Alembic.
revision = '2b3e9410ac43'
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
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('modified'),
    sa.UniqueConstraint('order'),
    sa.UniqueConstraint('user')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('app_board')
    ### end Alembic commands ###
