# backlog.py
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # make sure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import models

    return app
