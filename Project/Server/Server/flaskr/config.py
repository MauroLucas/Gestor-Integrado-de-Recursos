from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def app_setup():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bd_gir'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.add_url_rule('/', 'app.home')
    return app
