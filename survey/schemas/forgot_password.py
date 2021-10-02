from marshmallow import Schema, fields


class ForgotPasswordSchema(Schema):
    email = fields.String(required=True, description="Email")


class SetPasswordSchema(Schema):
    token = fields.String(required=True, description="Forgot password token")
    password = fields.String(required=True, description="New password")
