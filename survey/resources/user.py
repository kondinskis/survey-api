from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, current_user

from survey.services.user import UserService
from survey.schemas.user import (
    UserInSchema,
    UserOutSchema,
)
from survey.security import allowed_for


bp = Blueprint("user", __name__)


@bp.route("/<int:id>")
class User(MethodView):
    @bp.arguments(UserInSchema)
    @bp.response(200, schema=UserOutSchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, data, id):
        user = UserService.update(id, data)
        return user

    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    @bp.response(204)
    def delete(self, id):
        UserService.delete(id), 204

    @bp.response(200, schema=UserOutSchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def get(self, id):
        user = UserService.get(id)
        return user


@bp.route("")
class UserList(MethodView):
    @bp.response(200, schema=UserOutSchema(many=True))
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def get(self):
        users = UserService.get_all()
        return users

    @bp.arguments(UserOutSchema)
    @bp.response(201, schema=UserOutSchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def post(self, data):
        user = UserService.create(data)
        return user, 201


@bp.route("/register")
class UserRegister(MethodView):
    @bp.arguments(UserInSchema)
    @bp.response(201)
    def post(self):
        UserService.register(ns.payload)
        return {}, 201
