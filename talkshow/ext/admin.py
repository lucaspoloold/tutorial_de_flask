from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView

def configure(app):
    app.admin = Admin(app, "TalkShow", template_mode="bootstrap2")