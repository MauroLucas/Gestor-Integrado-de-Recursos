from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class AppSetup:

    def __init__(self):
        self.get_app()

    def get_app(self):
        # create and configure the app
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_mapping(
            SECRET_KEY='dev',
        )
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bd_gir'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def get_db(self):
        return SQLAlchemy(self.get_app())
