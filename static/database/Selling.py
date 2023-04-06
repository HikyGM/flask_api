import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Selling(SqlAlchemyBase):
    __tablename__ = 'selling'

    id_selling = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    product_on_sale = orm.relationship("Product_on_sale", back_populates='selling')
    id_provider = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('providers.id_provider'))
    provider = orm.relationship("Providers", back_populates='provider')
    total_price = sqlalchemy.Column(sqlalchemy.Float)
    date_sale = sqlalchemy.Column(sqlalchemy.Date)

