"""Added userEmail

Revision ID: e7aaeae07711
Revises: 
Create Date: 2021-04-27 16:33:07.840014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7aaeae07711'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('userEmail', sa.String(), nullable=False))
    op.alter_column('User', 'userName',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'User', ['userName'])
    op.create_unique_constraint(None, 'User', ['userEmail'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='unique')
    op.drop_constraint(None, 'User', type_='unique')
    op.alter_column('User', 'userName',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('User', 'userEmail')
    # ### end Alembic commands ###
