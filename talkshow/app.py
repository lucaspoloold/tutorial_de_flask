from flask import Flask
from talkshow.ext import cli, bootstrap
from talkshow.ext import db
from talkshow.blueprints import webui


def create_app():
    """Creates a new Flask app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    #extensions
    db.configure(app)
    cli.configure(app)
    bootstrap.configure(app)

    #blueprints
    webui.configure(app)

    return app
