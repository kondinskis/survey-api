from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user

from survey.namespaces.role import ns
from survey.services.role import RoleService
from survey.schemas.role import schema


@ns.route("")
class RoleList(Resource):
    @ns.marshal_with(schema, skip_none=True)
    @jwt_required
    def get(self):
        return RoleService.get_all()
