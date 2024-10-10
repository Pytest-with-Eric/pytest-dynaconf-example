from flask import Flask
from flask_app.routes import main
from dynaconf import FlaskDynaconf


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    FlaskDynaconf(app)

    app.register_blueprint(main)

    return app
