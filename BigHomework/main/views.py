#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/13/18.
from BigHomework import db
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.login import current_user
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
        page, per_page = current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out = False)
    posts = pagination.items

    return render_template('index.html')
