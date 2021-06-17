from flask import Flask

from survey.config import Config
from survey.extensions import init_extensions, api
from survey.resources.auth import ns as auth_ns
from survey.resources.user import ns as user_ns
from survey.resources.role import ns as role_ns
from survey.resources.survey import ns as survey_ns
from survey.resources.tag import ns as tag_ns
from survey.resources.forgot_password import ns as forgot_password_ns


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)

    api.add_namespace(auth_ns)
    api.add_namespace(role_ns)
    api.add_namespace(user_ns)
    api.add_namespace(survey_ns)
    api.add_namespace(tag_ns)
    api.add_namespace(forgot_password_ns)

    import survey.errors

    return app
