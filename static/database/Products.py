import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Products(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'products'

    id_products = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_product = sqlalchemy.Column(sqlalchemy.String(100), nullable=True)  # unique=True,
    article_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('category_product.id_category'))
    category_product = orm.relationship('Category_product')
    manufacturer = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('manufacturer_product.id_manufacturer'))
    manufacturer_product = orm.relationship('Manufacturer_product')
    property = orm.relationship("Property_product", back_populates='property_product')
    path_image = sqlalchemy.Column(sqlalchemy.String, default='static/images/nonePhoto.png')
