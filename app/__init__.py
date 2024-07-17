from flask import Flask

from app.plugins import initPlugins
from app.views import blue


def createApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CHBRg*9847bDvj@9.134.95.129:3306/dev'
    app.register_blueprint(blue, url_prefix='/app')
    initPlugins(app)

    return app
