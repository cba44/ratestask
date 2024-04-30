from flask import Flask

from app.api import RatesBlueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(RatesBlueprint)

    return app