"""Add description content type column to Python metadata

Revision ID: 295358ee27b1
Revises: d808ef831749
Create Date: 2019-10-22 10:32:06.842535+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '295358ee27b1'
down_revision = 'd808ef831749'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('python_package_metadata', sa.Column('description_content_type', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('python_package_metadata', 'description_content_type')
    # ### end Alembic commands ###
