#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/13/18.

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
