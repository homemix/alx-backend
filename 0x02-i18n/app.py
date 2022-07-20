#!/usr/bin/env python3
"""
A basic flask app to configure babel
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone
import pytz.exceptions

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get the user
    """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    Before request
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    The locale selector
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """determines correct time_zone"""
    t_zone = request.args.get('timezone', None)

    if t_zone:
        try:
            return timezone(t_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'

    default = app.config['BABEL_DEFAULT_TIMEZONE']

    return request.accept_languages.best_match(default)


@app.route('/')
def index():
    """
    The index page
    """
    g.time = format_datetime()
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
