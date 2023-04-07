import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Category_product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category_product'

    id_category = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title_category = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, unique=True)  # unique=True,
    category = orm.relationship("Products", back_populates='category_product')


