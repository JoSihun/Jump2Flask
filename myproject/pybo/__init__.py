""" WikiDocs Jump 2 Flask """
# Chapter 01-06 Hello, Pybo!
# https://wikidocs.net/81238

# Chapter 02-02 Flask Application Factory
# https://wikidocs.net/81504

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # DATABASE ORM
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # BLUEPRINT
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app