from flask import Blueprint, jsonify, current_app

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Basic route to show the current environment and database URL."""
    return jsonify(
        {
            "environment": current_app.config["ENV_FOR_DYNACONF"],
            "debug": current_app.config["DEBUG"],
            "database_url": current_app.config["DATABASE_URL"],
        }
    )
