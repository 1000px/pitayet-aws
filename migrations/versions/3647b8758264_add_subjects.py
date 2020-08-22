"""add subjects

Revision ID: 3647b8758264
Revises: 
Create Date: 2020-07-31 16:11:33.422842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3647b8758264'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('is_root', sa.Boolean(), nullable=True),
    sa.Column('is_leaf', sa.Boolean(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['subjects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subjects_name'), 'subjects', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subjects_name'), table_name='subjects')
    op.drop_table('subjects')
    # ### end Alembic commands ###
