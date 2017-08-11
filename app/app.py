from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap

from nav import nav
from auth import *
from flask_sqlalchemy import SQLAlchemy


def create_app():
    a = Flask(__name__)
    a.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    Bootstrap(a)
    nav.init_app(a)
    return a


app = create_app()
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/form/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        return render_template('form.html', result=processed_text)

    return render_template('form.html')


@app.route('/secret-page')
@requires_auth
def secret_page():
    return render_template('index.html')


@app.route('/user/')
def create_user():
    user = User('admin', 'admin@example.com')
    db.session.add(user)
    db.session.commit()


@app.route('/users/')
def get_users():
    users = User.query.all()
    return users


@app.route('/react/')
def react(name=None):
    return render_template('react.html')


if __name__ == '__main__':
    app.run()
