#!/usr/bin/env python3
"""
A basic flask app to configure babel
"""
from flask import Flask
from flask_babel import Babel


class Config(object):
    """
    The config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.template_folder = 'templates'
babel = Babel(app)
app.config.from_object(Config)
