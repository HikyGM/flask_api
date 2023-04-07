import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Manufacturer_product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'manufacturer_product'

    id_manufacturer = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_manufacturer = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, unique=True)  # unique=True,
    INN = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String(20), nullable=True)
    manufacturer = orm.relationship("Products", back_populates='manufacturer_product')
