from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, current_user

from survey.services.role import RoleService
from survey.schemas.role import RoleSchema

bp = Blueprint("role", __name__)


@bp.route("")
class RoleList(MethodView):
    @bp.response(200, schema=RoleSchema)
    @jwt_required()
    def get(self):
        return RoleService.get_all()
