"""empty message

Revision ID: c7ef90d85b5e
Revises: fa00de5da932
Create Date: 2023-04-27 21:33:55.521994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7ef90d85b5e'
down_revision = 'fa00de5da932'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.alter_column('startdate',
               existing_type=sa.DATE(),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('enddate',
               existing_type=sa.DATE(),
               type_=sa.String(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.alter_column('enddate',
               existing_type=sa.String(length=10),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.alter_column('startdate',
               existing_type=sa.String(length=10),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###
