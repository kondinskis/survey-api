from flask_restx import fields
from survey.namespaces.survey import ns
from .tag import schema as tag_schema

option_schema = ns.model(
    "Survey option schema",
    {
        "id": fields.Integer(description="Option unique id"),
        "option": fields.String(description="Option itself"),
        "order": fields.Integer(description="Option order"),
        "created_at": fields.DateTime(description="Date of creation"),
        "updated_at": fields.DateTime(description="Date of modification"),
        "total": fields.Integer(description="Option choosen as answer"),
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
        "options": fields.Nested(option_schema, as_list=True, skip_none=True),
        "total": fields.Integer(description="Total answers"),
    },
)

answer_schema = ns.model(
    "Survey answers schema",
    {
        "answers": fields.Nested(
            ns.model(
                "Survey answer schema",
                {
                    "question_id": fields.Integer(description="Question unique id"),
                    "option_id": fields.Integer(description="Option unique id"),
                },
            ),
            as_list=True,
        )
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
        "questions": fields.Nested(question_schema, as_list=True, skip_none=True),
        "tag_ids": fields.List(fields.Integer),
        "tags": fields.Nested(tag_schema, as_list=True, skip_none=True),
        "published": fields.Boolean(description="Indicates if the survey is published"),
        "login_required": fields.Boolean(
            description="Indicates if login is required in order to take survey"
        ),
    },
)
