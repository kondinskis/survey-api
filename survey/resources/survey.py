from flask_restx import Resource
from flask_jwt_extended import jwt_required, current_user

from survey.namespaces.survey import ns
from survey.services.survey import SurveyService
from survey.schemas.survey import schema


@ns.route("/<id>")
@ns.param("id", "Survey unique identifier")
class Survey(Resource):
    @ns.marshal_with(schema)
    @ns.expect(schema)
    @jwt_required
    def put(self, id):
        survey = SurveyService.update(id, ns.payload)
        return survey

    @jwt_required
    def delete(self, id):
        SurveyService.delete(id)

    @ns.marshal_with(schema)
    @jwt_required
    def get(self, id):
        survey = SurveyService.get(id)
        return survey


@ns.route("")
class SurveyList(Resource):
    @ns.marshal_list_with(schema)
    @jwt_required
    def get(self):
        surveys = SurveyService.get_all()
        return surveys

    @ns.marshal_with(schema)
    @ns.expect(schema)
    @jwt_required
    def post(self):
        survey = SurveyService.create(ns.payload)
        return survey, 201