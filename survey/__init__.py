from flask import Flask

from survey.config import Config
from survey.extensions import init_extensions, api
from survey.resources.user import ns as user_ns
from survey.resources.role import ns as role_ns


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)

    api.add_namespace(role_ns)
    api.add_namespace(user_ns)

    return app