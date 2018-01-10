"""adding status and intrested in

Revision ID: 24f3b7a553c0
Revises: 27bbd998fdf9
Create Date: 2018-01-10 03:43:25.017075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24f3b7a553c0'
down_revision = '27bbd998fdf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('intrested_in', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'intrested_in')
    # ### end Alembic commands ###