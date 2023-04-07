import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Providers(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'providers'

    id_provider = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    provider = orm.relationship("Selling")
    first_name_provider = sqlalchemy.Column(sqlalchemy.String(50))
    last_name_provider = sqlalchemy.Column(sqlalchemy.String(50))
    day_of_birth = sqlalchemy.Column(sqlalchemy.Date)
    gender_provider = sqlalchemy.Column(sqlalchemy.String(50))
    path_im_provider = sqlalchemy.Column(sqlalchemy.String(50), default='up.png')
    phone_number = sqlalchemy.Column(sqlalchemy.String(50))
    city_provider = sqlalchemy.Column(sqlalchemy.String(50))
