#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/13/18.
from flask import render_template

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
