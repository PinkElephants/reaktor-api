"""spotify v3

Revision ID: c3644d9e24fd
Revises: aa20abc765b2
Create Date: 2022-11-05 14:20:16.124579

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c3644d9e24fd'
down_revision = 'aa20abc765b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('spotify_expires', sa.Integer(), nullable=True))
    op.drop_column('user', 'access_spotify_expires')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('access_spotify_expires', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('user', 'spotify_expires')
    # ### end Alembic commands ###
