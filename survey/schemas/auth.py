from flask_restx import fields
from survey.namespaces.auth import ns

token_request_schema = ns.model(
    "Access token request schema",
    {
        "email": fields.String(required=True, description="Email"),
        "password": fields.String(required=True, description="Password"),
    },
)

token_schema = ns.model(
    "Access token schema",
    {
        "access_token": fields.String(description="JWT token"),
        "refresh_token": fields.String(description="Refresh access token"),
    },
)
