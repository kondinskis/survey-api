from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user

from survey.namespaces.tag import ns
from survey.services.tag import TagService
from survey.schemas.tag import schema
from survey.security import allowed_for


@ns.route("/<id>")
@ns.param("id", "Tag unique identifier")
class Tag(Resource):
    @ns.marshal_with(schema, skip_none=True)
    @ns.expect(schema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, id):
        tag = TagService.update(id, ns.payload)
        return tag

    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def delete(self, id):
        TagService.delete(id), 204

    @ns.marshal_with(schema, skip_none=True)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def get(self, id):
        tag = TagService.get(id)
        return tag


@ns.route("")
class TagList(Resource):
    @ns.marshal_list_with(schema, skip_none=True)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def get(self):
        tags = TagService.get_all()
        return tags

    @ns.marshal_with(schema, skip_none=True)
    @ns.expect(schema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def post(self):
        tag = TagService.create(ns.payload)
        return tag, 201
