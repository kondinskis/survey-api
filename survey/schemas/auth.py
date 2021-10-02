from marshmallow import Schema, fields


class TokenRequestSchema(Schema):
    email = fields.String(required=True, description="Email")
    password = fields.String(required=True, description="Password")


class TokenSchema(Schema):
    access_token = fields.String(description="JWT token")
    refresh_token = fields.String(description="Refresh access token")
