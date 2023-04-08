import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Blog(SqlAlchemyBase, SerializerMixin ):
    __tablename__ = 'blog'

    id_post = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_post = sqlalchemy.Column(sqlalchemy.String(100), )
    author_post = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id_user'))
    data_time_post = sqlalchemy.Column(sqlalchemy.DateTime)
    url_post = sqlalchemy.Column(sqlalchemy.String(150))
    path_im_post = sqlalchemy.Column(sqlalchemy.String(150))
    text_post = sqlalchemy.Column(sqlalchemy.Text)
    author = orm.relationship('User')
