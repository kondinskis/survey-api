from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

api = Api(version="0.0.1", title="Survey", description="Survey API", validate=True)
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
jwt = JWTManager()


def init_extensions(app):
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
