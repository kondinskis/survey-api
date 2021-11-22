from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, current_user

from survey.schemas.forgot_password import (
    ForgotPasswordSchema,
    SetPasswordSchema,
)
from survey.services.user import UserService

bp = Blueprint("forgot_password", __name__)


@bp.route("")
class ForgotPassword(MethodView):
    @bp.arguments(ForgotPasswordSchema)
    @bp.response(201)
    def post(self, data):
        UserService.forgot_password(data["email"])
        return {}, 201


@bp.route("/set")
class SetPassword(MethodView):
    @bp.arguments(SetPasswordSchema)
    @bp.response(200)
    def post(self, data):
        UserService.set_password(data["token"], data["password"])
        return {}, 200
