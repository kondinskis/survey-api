from flask import Flask

from survey.config import Config
from survey.extensions import init_extensions, api


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)

    return app