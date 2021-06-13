from flask_restx import fields
from survey.namespaces.tag import ns

schema = ns.model(
    "Tag schema",
    {
        "id": fields.Integer(
            readOnly=True, description="The tag unique identifier"
        ),
        "title": fields.String(required=True, description="Tag title"),
        "description": fields.String(
            required=True, description="Tag description"
        ),
        "created_at": fields.DateTime(description="Date of creation"),
        "updated_at": fields.DateTime(description="Date of modification"),
    },
)
