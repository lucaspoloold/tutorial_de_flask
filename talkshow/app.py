from flask import Flask
from talkshow.ext import cli, bootstrap, admin, apidocs
from talkshow.ext import db
from talkshow.blueprints import webui, restapi


def create_app():
    """Creates a new Flask app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    #extensions
    db.configure(app)
    cli.configure(app)
    bootstrap.configure(app)
    admin.configure(app)
    apidocs.configure(app)

    #blueprints
    webui.configure(app)
    restapi.configure(app)

    return app
