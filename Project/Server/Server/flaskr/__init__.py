import os

from flask import Flask, render_template, Blueprint
from . import auth
from flask_sqlalchemy import SQLAlchemy
from config import app_setup


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def home():
    return render_template('home.html')


def create_app(test_config=None):
    # create and configure the app
    app = app_setup()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)
    app.register_blueprint(bp)

    return app
