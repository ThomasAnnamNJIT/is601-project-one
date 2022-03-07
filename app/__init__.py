from flask import Flask

from app.content import content


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(content)
    return app
