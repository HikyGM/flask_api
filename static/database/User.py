import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id_user = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, unique=True)  # unique=True,
    password_user = sqlalchemy.Column(sqlalchemy.String(256), nullable=True)
    email_user = sqlalchemy.Column(sqlalchemy.String(50), index=True, unique=True, nullable=True)
    first_name_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    last_name_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    day_of_birth = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    gender_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    path_im_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True, default='static/images/nonePhoto.png')
    phone_number = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    city_user = sqlalchemy.Column(sqlalchemy.String(50), nullable=True)
    type_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('type_users.id_type'), default=3)
    type_u = orm.relationship('Type_users')
    blog = orm.relationship("Blog", back_populates='author')
    # id = id_user

    def set_password(self, password):
        self.password_user = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_user, password)

