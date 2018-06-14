#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/14/18.
from flask.ext.pagedown.fields import PageDownField
from flask.ext.wtf import Form
from wtforms import SubmitField, StringField
from wtforms.validators import Required


class PostForm(Form):
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')



class CommentForm(Form):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')
