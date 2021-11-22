from flask.views import MethodView
from flask_smorest import Blueprint

from werkzeug.exceptions import Unauthorized
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    current_user,
)

from survey.services.user import UserService
from survey.schemas.auth import (
    TokenRequestSchema,
    TokenSchema,
)
from survey.extensions import jwt


@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {"role": user.role.name}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user = UserService.get_by_email(jwt_data["sub"])
    return user


bp = Blueprint("auth", __name__)


@bp.route("/token")
class AccessToken(MethodView):
    @bp.arguments(TokenRequestSchema)
    @bp.response(200, schema=TokenSchema)
    def post(self, data):

        user = UserService.get_by_email(data["email"])

        if user is None:
            raise Unauthorized(description="Wrong email or password")

        if not user.verify_password(data["password"]):
            raise Unauthorized(description="Wrong email or password")

        ret = {
            "access_token": create_access_token(identity=user),
            "refresh_token": create_refresh_token(identity=user),
        }
        return ret


@bp.route("/refresh")
class RefreshToken(MethodView):
    @bp.response(200, schema=TokenSchema)
    @jwt_required(refresh=True)
    def post(self):
        ret = {"access_token": create_access_token(identity=current_user)}
        return ret
