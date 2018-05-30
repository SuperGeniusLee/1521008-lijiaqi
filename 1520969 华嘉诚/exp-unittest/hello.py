import os
from datetime import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import DateTime
from sqlalchemy.orm import session
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.INT, primary_key = True)
    username = db.Column(db.String(64))

    def __init__(self, username, age=20):
        self.username = username
        self.age = age

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    content = StringField('What is on your mind?', validators = [DataRequired()])
    name = StringField('Author?', validators = [DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500





    return render_template('index.html', form = form, posts = posts)


if __name__ == '__main__':
    app.run(debug = True, port = 8080)
    # pass
