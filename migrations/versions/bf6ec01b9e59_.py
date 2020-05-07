"""empty message

Revision ID: bf6ec01b9e59
Revises: ce2cca496c24
Create Date: 2020-05-04 15:06:50.080377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf6ec01b9e59'
down_revision = 'ce2cca496c24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('import_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('match', 'import_id')
    # ### end Alembic commands ###
