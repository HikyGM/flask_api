from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

application = Flask(__name__)
api = Api(application)
login_manager = LoginManager()
login_manager.init_app(application)
application.config['SECRET_KEY'] = 'bfy45ue7iuyilutgbkwycu4b7e46ytwu4etriuw34yiuitwyeiut54'
