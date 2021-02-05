from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user

from survey.namespaces.user import ns
from survey.services.user import UserService
from survey.schemas.user import schema


@ns.route("/<id>")
@ns.param("id", "User unique identifier")
class User(Resource):
    @ns.marshal_with(schema)
    @ns.expect(schema)
    @jwt_required
    def put(self, id):
        user = UserService.update(id, ns.payload)
        return user

    @jwt_required
    def delete(self, id):
        UserService.delete(id), 204

    @ns.marshal_with(schema)
    @jwt_required
    def get(self, id):
        user = UserService.get(id)
        return user


@ns.route("")
class UserList(Resource):
    @ns.marshal_list_with(schema)
    @jwt_required
    def get(self):
        users = UserService.get_all()
        return users

    @ns.marshal_with(schema)
    @ns.expect(schema)
    @jwt_required
    def post(self):
        user = UserService.create(ns.payload)
        return user, 201