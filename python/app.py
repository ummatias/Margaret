
from flask import Flask
from python.models.subscribed import Subscribed
from python.models.user import User
from python.models.project import Project
from python.ext.organization import organization

def create_app():
    app = Flask(__name__)
    organization.init_app(app)
    return app

