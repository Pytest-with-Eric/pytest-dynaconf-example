from flask import Flask
from flask_app.config import init_app
from flask_app.routes import main


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Initialize Dynaconf
    init_app(app)

    # Register the routes
    app.register_blueprint(main)

    return app
