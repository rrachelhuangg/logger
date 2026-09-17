import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SITE_NAME"] = os.environ.get("SITE_NAME", "life logger")

    from .routes import bp

    app.register_blueprint(bp)

    return app
