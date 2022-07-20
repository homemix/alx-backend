#!/usr/bin/env python3
"""
A basic flask app to configure babel
"""
from flask_babel import Babel
from flask import Flask, render_template, request

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


@babel.localeselector
def get_locale():
    """
    The locale selector
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    The index page
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
