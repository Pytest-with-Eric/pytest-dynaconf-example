from dynaconf import FlaskDynaconf


def init_app(app):
    """Initialize Dynaconf with Flask app."""
    FlaskDynaconf(app, settings_files=["src/flask_app/settings.toml"])
