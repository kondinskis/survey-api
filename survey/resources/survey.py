from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, current_user

from survey.services.survey import SurveyService
from survey.schemas.survey import (
    AnswerSchema,
    AnswersListSchema,
    SurveySchema,
)
from survey.security import allowed_for

bp = Blueprint("survey", __name__)


@bp.route("/<int:id>")
class Survey(MethodView):
    @bp.arguments(SurveySchema)
    @bp.response(200, schema=SurveySchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, data, id):
        survey = SurveyService.update(id, data)
        return survey

    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    @bp.response(204)
    def delete(self, id):
        SurveyService.delete(id), 204

    @bp.response(200, schema=SurveySchema)
    @jwt_required(optional=True)
    def get(self, id):
        survey = SurveyService.get(id)
        return survey


@bp.route("")
class SurveyList(MethodView):
    @bp.response(200, schema=SurveySchema(many=True))
    @jwt_required(optional=True)
    def get(self):
        surveys = SurveyService.get_all()
        return surveys

    @bp.arguments(SurveySchema)
    @bp.response(201, schema=SurveySchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def post(self, data):
        survey = SurveyService.create(data)
        return survey, 201


@bp.route("/<int:id>/take")
class TakeSurvey(MethodView):
    @jwt_required(optional=True)
    @bp.response(200)
    def get(self, id):
        SurveyService.check_take(id)
        return {}, 200

    @bp.arguments(AnswersListSchema)
    @bp.response(201)
    @jwt_required(optional=True)
    def post(self, data, id):
        SurveyService.take(id, data["answers"])
        return {}, 201


@bp.route("/<int:id>/results")
class SurveyResults(MethodView):
    @bp.response(200, schema=SurveySchema)
    @jwt_required(optional=True)
    def get(self, id):
        return SurveyService.results(id)


@bp.route("/<int:id>/publish")
class SurveyPublish(MethodView):
    @bp.response(200, schema=SurveySchema)
    @jwt_required()
    @allowed_for("SYSTEM", "ADMIN")
    def put(self, id):
        return SurveyService.publish(id)
