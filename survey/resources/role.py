from flask_restx import Resource

from survey.namespaces.role import ns
from survey.services.role import RoleService
from survey.schemas.role import schema


@ns.route("")
class RoleList(Resource):
    @ns.marshal_with(schema)
    def get(self):
        return RoleService.get_all()