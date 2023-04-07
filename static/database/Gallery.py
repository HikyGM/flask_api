import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Gallery(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'gallery'

    id_gallery = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    path_im = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
