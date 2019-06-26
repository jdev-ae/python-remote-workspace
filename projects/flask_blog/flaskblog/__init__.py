from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '6d0e21d41cbc2309e3656ab929ad21f2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev_db.db'

db = SQLAlchemy(app)

from flaskblog import routes
