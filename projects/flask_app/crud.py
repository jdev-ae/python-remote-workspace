import os

from flask import Flask, request, jsonify
# flask-marshmallow to rendered json response
from flask_marshmallow import Marshmallow
# ORM
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# flask config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# for db config
db = SQLAlchemy(app)

# for json serialize or deserialize
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@app.route('/user', methods=['GET'])
def get_all():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


if __name__ == '__main__':
    app.run(debug=True)
