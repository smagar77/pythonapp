"""empty message

Revision ID: 4457cf26378b
Revises: bf6ec01b9e59
Create Date: 2020-05-04 22:06:34.032383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4457cf26378b'
down_revision = 'bf6ec01b9e59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deliveries', sa.Column('bowling_team', sa.String(length=255), nullable=True))
    op.add_column('deliveries', sa.Column('fielder', sa.String(length=255), nullable=True))
    op.drop_column('deliveries', 'filder')
    op.drop_column('deliveries', 'bowing_team')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deliveries', sa.Column('bowing_team', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('deliveries', sa.Column('filder', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('deliveries', 'fielder')
    op.drop_column('deliveries', 'bowling_team')
    # ### end Alembic commands ###
