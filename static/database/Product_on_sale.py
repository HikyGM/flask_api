import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Product_on_sale(SqlAlchemyBase):
    __tablename__ = 'product_on_sale'

    id_product_on_sale = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    id_selling = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('selling.id_selling'))
    selling = orm.relationship('Selling')
    id_product = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id_products'))
    product = orm.relationship('Products')


