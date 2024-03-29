"""adds published flag

Revision ID: d23445bc6f67
Revises: 37a3865cf5c2
Create Date: 2021-06-09 22:51:24.997248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd23445bc6f67'
down_revision = '37a3865cf5c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('published', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey', 'published')
    # ### end Alembic commands ###
