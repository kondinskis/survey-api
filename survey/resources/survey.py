from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user

from survey.namespaces.survey import ns
from survey.services.survey import SurveyService
from survey.schemas.survey import schema, answer_schema
from survey.security import allowed_for


@ns.route("/<int:id>")
@ns.param("id", "Survey unique identifier")
class Survey(Resource):
    @ns.marshal_with(schema, skip_none=True)
    @ns.expect(schema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, id):
        survey = SurveyService.update(id, ns.payload)
        return survey

    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def delete(self, id):
        SurveyService.delete(id), 204

    @ns.marshal_with(schema, skip_none=True)
    @jwt_required(optional=True)
    def get(self, id):
        survey = SurveyService.get(id)
        return survey


@ns.route("")
class SurveyList(Resource):
    @ns.marshal_list_with(schema, skip_none=True)
    @jwt_required(optional=True)
    def get(self):
        surveys = SurveyService.get_all()
        return surveys

    @ns.marshal_with(schema, skip_none=True)
    @ns.expect(schema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def post(self):
        survey = SurveyService.create(ns.payload)
        return survey, 201


@ns.route("/<int:id>/take")
class TakeSurvey(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        SurveyService.check_take(id)
        return {}, 200

    @ns.expect(answer_schema)
    @jwt_required(optional=True)
    def post(self, id):
        SurveyService.take(id, ns.payload["answers"])
        return {}, 201


@ns.route("/<int:id>/results")
class SurveyResults(Resource):
    @ns.marshal_with(schema)
    @jwt_required(optional=True)
    def get(self, id):
        return SurveyService.results(id)


@ns.route("/<int:id>/publish")
class SurveyPublish(Resource):
    @ns.marshal_with(schema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, id):
        return SurveyService.publish(id)
