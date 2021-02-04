from flask_restx import Resource

from survey.namespaces.user import ns
from survey.services.user import UserService


@ns.route()
class UserList(Resource):
    def get(self):
        UserService.create({})