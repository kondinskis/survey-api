from werkzeug.exceptions import NotFound, BadRequest
from survey.models.survey import Survey
from survey.models.question import Question
from survey.models.option import Option
from survey.models.answer import Answer


class SurveyService:
    @staticmethod
    def create(survey):
        pass

    @staticmethod
    def update(id, survey):
        pass

    @staticmethod
    def delete(id):
        pass

    @staticmethod
    def get(id):
        pass

    @staticmethod
    def get_all():
        pass
