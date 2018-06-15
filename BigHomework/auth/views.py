#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/13/18.
from . import auth
from auth.forms import LoginForm, RegistrationForm
from flask import flash
from flask import render_template
from flask import request
from flask import url_for
from flask.ext.login import login_required, login_user, logout_user
from models import User
from BigHomework import db
from werkzeug.utils import redirect


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('login.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect("/")


@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your registration was successful!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form = form)
