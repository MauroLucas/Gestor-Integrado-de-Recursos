import os

from flask import Flask, render_template, Blueprint, session, url_for, redirect
from . import auth
from . import ControladorLogin,ControladorRegistrarUsuario,ControladorAgregarRecurso
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('auth.login_succesful'))
    return render_template('home.html')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/gir'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

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

    app.register_blueprint(ControladorLogin.urlLogin)
    app.register_blueprint(ControladorRegistrarUsuario.urlRegistrarUsuario)
    app.register_blueprint(ControladorAgregarRecurso.urlAgregarRecurso)


    return app
