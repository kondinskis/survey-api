from flask_restx import fields
from survey.namespaces.forgot_password import ns

forgot_password_request = ns.model(
    "Forgot password request schema",
    {
        "email": fields.String(description="Email", required=True),
    },
)

set_password = ns.model(
    "Set password schema",
    {
        "token": fields.String(
            description="Forgot password token", required=True
        ),
        "password": fields.String(description="New password", required=True),
    },
)
