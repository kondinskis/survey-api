from flask_restx import Resource

from werkzeug.exceptions import Unauthorized
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    current_user,
)

from survey.services.user import UserService
from survey.namespaces.auth import ns
from survey.schemas.auth import token_request_schema, token_schema
from survey.extensions import jwt


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {"role": user.role.name}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    user = UserService.get_by_email(identity)
    return user


@ns.route("/token")
class AccessToken(Resource):
    @ns.marshal_with(token_schema)
    @ns.expect(token_request_schema)
    def post(self):

        user = UserService.get_by_email(ns.payload["email"])

        if user is None:
            raise Unauthorized(description="Wrong email or password")

        if not user.verify_password(ns.payload["password"]):
            raise Unauthorized(description="Wrong email or password")

        ret = {
            "access_token": create_access_token(identity=user),
            "refresh_token": create_refresh_token(identity=user),
        }
        return ret


@ns.route("/refresh")
class RefreshToken(Resource):
    @ns.marshal_with(token_schema)
    @jwt_refresh_token_required
    def post(self):
        ret = {"access_token": create_access_token(identity=current_user)}
        return ret
