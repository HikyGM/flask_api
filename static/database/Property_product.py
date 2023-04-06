import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Property_product(SqlAlchemyBase):
    __tablename__ = 'property_product'

    id_property = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_product = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id_products'))
    property_product = orm.relationship('Products')
    title_property = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)  # unique=True,
    title_value = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)
