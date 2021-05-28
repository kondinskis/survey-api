from flask_restx import fields
from survey.namespaces.user import ns
from .role import schema as role_schema

schema = ns.model(
    "User schema",
    {
        "id": fields.Integer(readOnly=True, description="The user unique identifier"),
        "firstname": fields.String(required=True, description="First name"),
        "lastname": fields.String(required=True, description="Last name"),
        "email": fields.String(required=True, description="User email"),
        "password": fields.String(description="Password"),
        "role_id": fields.Integer(required=True, description="Role unique id"),
        "role": fields.Nested(role_schema),
        "created_at": fields.DateTime(description="Date of creation"),
        "updated_at": fields.DateTime(description="Date of modification"),
    },
)
