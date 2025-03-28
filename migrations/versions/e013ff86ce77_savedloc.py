"""savedloc

Revision ID: e013ff86ce77
Revises: 251faca4ba9a
Create Date: 2025-03-24 09:31:55.718120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e013ff86ce77'
down_revision = '251faca4ba9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('savedlocs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('location_name', sa.String(length=255), nullable=False),
    sa.Column('lat', sa.Float(precision=6), nullable=False),
    sa.Column('long', sa.Float(precision=6), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('home_lat',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=True)
        batch_op.alter_column('home_long',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=True)
        batch_op.alter_column('work_lat',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=True)
        batch_op.alter_column('work_long',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=6),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('work_long',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('work_lat',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('home_long',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=True)
        batch_op.alter_column('home_lat',
               existing_type=sa.Float(precision=6),
               type_=sa.REAL(),
               existing_nullable=True)

    op.drop_table('savedlocs')
    # ### end Alembic commands ###
