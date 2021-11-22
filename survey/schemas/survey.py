from marshmallow import Schema, fields
from .tag import TagSchema


class OptionSchema(Schema):
    id = fields.Integer(description="Option unique id")
    option = fields.String(description="Option itself")
    order = fields.Integer(description="Option order")
    created_at = fields.DateTime(description="Date of creation")
    updated_at = fields.DateTime(description="Date of modification")
    total = fields.Integer(description="Option choosen as answer")


class QuestionSchema(Schema):
    id = fields.Integer(description="Question unique id")
    question = fields.String(description="Question itself")
    order = fields.Integer(description="Question order")
    created_at = fields.DateTime(description="Date of creation")
    updated_at = fields.DateTime(description="Date of modification")
    options = fields.Nested(OptionSchema, many=True)
    total = fields.Integer(description="Total answers")


class AnswerSchema(Schema):
    question_id = fields.Integer(description="Question unique id")
    option_id = fields.Integer(description="Option unique id")


class AnswersListSchema(Schema):
    answers = fields.Nested(AnswerSchema, many=True)


class SurveySchema(Schema):
    id = fields.Integer(description="Survey unique id")
    title = fields.String(description="Survey title")
    description = fields.String(description="Survey description")
    active_till = fields.DateTime(description="Survey active till")
    active_from = fields.DateTime(description="Survey active from")
    created_at = fields.DateTime(description="Date of creation")
    updated_at = fields.DateTime(description="Date of modification")
    questions = fields.Nested(QuestionSchema, many=True)
    tag_ids = fields.List(fields.Integer)
    tags = fields.Nested(TagSchema, many=True)
    published = fields.Boolean(
        description="Indicates if the survey is published"
    )
    login_required = fields.Boolean(
        description="Indicates if login is required in order to take survey"
    )
