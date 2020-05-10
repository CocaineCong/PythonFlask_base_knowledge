"""empty message

Revision ID: 9c5a3528c076
Revises: fd77976701fc
Create Date: 2017-12-03 19:21:18.682283

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9c5a3528c076'
down_revision = 'fd77976701fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cms_role_user')
    op.drop_table('cms_role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_role',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('desc', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.Column('permissions', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('cms_role_user',
    sa.Column('cms_role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('cms_user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['cms_role_id'], ['cms_role.id'], name='cms_role_user_ibfk_1'),
    sa.ForeignKeyConstraint(['cms_user_id'], ['cms_user.id'], name='cms_role_user_ibfk_2'),
    sa.PrimaryKeyConstraint('cms_role_id', 'cms_user_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
