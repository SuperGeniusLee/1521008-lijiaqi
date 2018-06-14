#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/13/18.
from BigHomework import db
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.login import current_user, login_required
from main.forms import PostForm
from models import Post

from . import main


@main.route('/', methods = ['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body = form.body.data,
                    author = current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type = int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page = 10,
        error_out = False)
    posts = pagination.items
    return render_template('index.html', form = form, posts = posts, pagination = pagination)


@main.route('/user/<username>')
def user(username):
    # todo
    return redirect(url_for("main.index"))


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    # todo
    return redirect(url_for("main.index"))


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    # todo
    return redirect(url_for("main.index"))