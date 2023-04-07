import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Type_users(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'type_users'

    id_type = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_type = sqlalchemy.Column(sqlalchemy.String(20), unique=True, nullable=True)
    user = orm.relationship("User", back_populates='type_u')
