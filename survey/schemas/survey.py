from flask_restx import fields
from survey.namespaces.survey import ns

option_schema = ns.model(
    "Survey option schema",
    {
        "id": fields.Integer(description="Option unique id"),
        "option": fields.String(description="Option itself"),
        "order": fields.Integer(description="Option order"),
        "created_at": fields.DateTime(description="Date of creation"),
        "updated_at": fields.DateTime(description="Date of modification"),
    },
)

question_schema = ns.model(
    "Survey question schema",
    {
        "id": fields.Integer(description="Question unique id"),
        "question": fields.String(description="Question itself"),
        "order": fields.Integer(description="Question order"),
        "created_at": fields.DateTime(description="Date of creation"),
        "updated_at": fields.DateTime(description="Date of modification"),
        "options": fields.Nested(option_schema, as_list=True),
    },
)

schema = ns.model(
    "Survey schema",
    {
        "id": fields.Integer(description="Survey unique id"),
        "title": fields.String(description="Survey title"),
        "description": fields.String(description="Survey description"),
        "active_till": fields.DateTime(description="Survey active till"),
        "active_from": fields.DateTime(description="Survey active from"),
        "created_at": fields.DateTime(description="Date of creation"),
        "updated_at": fields.DateTime(description="Date of modification"),
        "questions": fields.Nested(question_schema, as_list=True),
    },
)