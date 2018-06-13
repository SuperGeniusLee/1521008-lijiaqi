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


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.INT, primary_key = True)
    username = db.Column(db.String(64))
    content = db.Column(db.String(100))
    time = db.Column(DateTime, default = datetime.now())

    def __repr__(self):
        return '<Post %r>' % self.username


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


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        content = (form.content.data)
        username = (form.name.data)
        post = Post()
        post.username = username
        post.content = content
        post.time = datetime.now()
        db.session.add(post)
        db.session.commit()

    posts = db.session.query(Post).all()  # type: list
    posts.reverse()

    return render_template('index.html', form = form, posts = posts)


if __name__ == '__main__':
    app.run(debug = True, port = 8080)
    # pass
