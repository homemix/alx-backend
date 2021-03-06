#!/usr/bin/env python3
"""
A basic flask app to configure babel
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.template_folder = 'templates'
babel = Babel(app)


class Config(object):
    """
    The config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    The index page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
