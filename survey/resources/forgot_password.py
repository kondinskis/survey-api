from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user

from survey.namespaces.forgot_password import ns
from survey.schemas.forgot_password import (
    forgot_password_request,
    set_password,
)
from survey.services.user import UserService


@ns.route("")
class ForgotPassword(Resource):
    @ns.expect(forgot_password_request)
    def post(self):
        UserService.forgot_password(ns.payload["email"])
        return {}, 201


@ns.route("/set")
class SetPassword(Resource):
    @ns.expect(set_password)
    def post(self):
        UserService.set_password(ns.payload["token"], ns.payload["password"])
        return {}, 200
