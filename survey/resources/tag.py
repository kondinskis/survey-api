from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, current_user

from survey.services.tag import TagService
from survey.schemas.tag import TagSchema
from survey.security import allowed_for

bp = Blueprint("tag", __name__)


@bp.route("/<int:id>")
class Tag(MethodView):
    @bp.arguments(TagSchema)
    @bp.response(200, schema=TagSchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, data, id):
        tag = TagService.update(id, data)
        return tag

    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    @bp.response(204)
    def delete(self, id):
        TagService.delete(id), 204

    @bp.response(200, schema=TagSchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def get(self, id):
        tag = TagService.get(id)
        return tag


@bp.route("")
class TagList(MethodView):
    @bp.response(200, schema=TagSchema(many=True))
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def get(self):
        tags = TagService.get_all()
        return tags

    @bp.arguments(TagSchema)
    @bp.response(200, schema=TagSchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def post(self, data):
        tag = TagService.create(data)
        return tag, 201
