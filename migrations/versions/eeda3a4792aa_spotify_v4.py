"""spotify v4

Revision ID: eeda3a4792aa
Revises: c3644d9e24fd
Create Date: 2022-11-05 14:20:58.002249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeda3a4792aa'
down_revision = 'c3644d9e24fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('access_spotify_expires', sa.Integer(), nullable=True))
    op.drop_column('user', 'spotify_expires')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('spotify_expires', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('user', 'access_spotify_expires')
    # ### end Alembic commands ###