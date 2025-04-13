"""update column name

Revision ID: 96c0e06d0376
Revises: e2213319c554
Create Date: 2025-04-12 21:26:46.366917

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '96c0e06d0376'
down_revision = 'e2213319c554'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('distance_queries', schema=None) as batch_op:
        batch_op.alter_column('distance_km',
               new_column_name='distance',
               existing_type=sa.Float(),
               existing_nullable=False)
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('now()'),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('distance_queries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('distance_km', mysql.FLOAT(), nullable=False))
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               server_default=sa.text('(now())'),
               existing_nullable=True)
        batch_op.drop_column('distance')

    # ### end Alembic commands ###
