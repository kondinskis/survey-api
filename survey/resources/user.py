from flask_restx import Resource

from survey.namespaces.user import ns
from survey.services.user import UserService
from survey.schemas.user import schema


@ns.route("/<id>")
@ns.param("id", "User unique identifier")
class User(Resource):
    @ns.marshal_with(schema)
    @ns.expect(schema)
    def put(self, id):
        user = UserService.update(id, ns.payload)
        return user

    def delete(self, id):
        UserService.delete(id)

    @ns.marshal_with(schema)
    def get(self, id):
        user = UserService.get(id)
        return user


@ns.route("")
class UserList(Resource):
    @ns.marshal_list_with(schema)
    def get(self):
        users = UserService.get_all()
        return users

    @ns.marshal_with(schema)
    @ns.expect(schema)
    def post(self):
        user = UserService.create(ns.payload)
        return user, 201