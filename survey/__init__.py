from flask import Flask

from survey.config import Config
from survey.extensions import init_extensions, api
from survey.resources.auth import bp as auth_bp
from survey.resources.user import bp as user_bp
from survey.resources.role import bp as role_bp
from survey.resources.survey import bp as survey_bp
from survey.resources.tag import bp as tag_bp
from survey.resources.forgot_password import bp as forgot_password_bp


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)

    api.register_blueprint(auth_bp, url_prefix="/auth")
    api.register_blueprint(role_bp, url_prefix="/roles")
    api.register_blueprint(user_bp, url_prefix="/users")
    api.register_blueprint(survey_bp, url_prefix="/surveys")
    api.register_blueprint(tag_bp, url_prefix="/tags")
    api.register_blueprint(forgot_password_bp, url_prefix="/forgot-password")

    # import survey.errors

    return app
