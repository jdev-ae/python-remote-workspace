from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '6d0e21d41cbc2309e3656ab929ad21f2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev_db.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
