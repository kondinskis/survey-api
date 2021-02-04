from flask_restx import fields
from survey.namespaces.role import ns

schema = ns.model(
    "Role schema",
    {
        "id": fields.Integer(readOnly=True, description="The role unique identifier"),
        "name": fields.String(description="Name"),
    },
)
