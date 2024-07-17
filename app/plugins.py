from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def initPlugins(app):
    db.init_app(app)
