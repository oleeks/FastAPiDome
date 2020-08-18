"""add user_id

Revision ID: b366a8494641
Revises: 5a5ca20e7fd1
Create Date: 2020-07-29 15:22:29.042937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b366a8494641'
down_revision = '5a5ca20e7fd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_id', sa.String(length=32), nullable=True, comment='用户id'))
    op.create_unique_constraint(None, 'user', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'user_id')
    # ### end Alembic commands ###