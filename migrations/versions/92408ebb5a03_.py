"""empty message

Revision ID: 92408ebb5a03
Revises: 
Create Date: 2018-04-07 15:35:36.745502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92408ebb5a03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=10000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('businesses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business_name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('posted_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('business_name')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.Column('posted_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('businesses')
    op.drop_table('users')
    # ### end Alembic commands ###