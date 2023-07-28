from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pinterest.db"
app.config["SECRET_KEY"] = "b65ef8da938312e02784e9c0f37c955e3d030f52cdb7afe3c9c913190223"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# vou precisar criar um pagina de login e uma rota  para ela
login_manager.login_view = "login"

from pinterest import routes