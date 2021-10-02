from marshmallow import Schema, fields
from .role import RoleSchema


class UserInSchema(Schema):
    firstname = fields.String(required=True, description="First name")
    lastname = fields.String(required=True, description="Last name")
    email = fields.String(required=True, description="User email")
    password = fields.String(required=True, description="Password")


class UserOutSchema(Schema):
    id = fields.Integer(description="The user unique identifier")
    firstname = fields.String(description="First name")
    lastname = fields.String(description="Last name")
    email = fields.String(description="User email")
    password = fields.String(description="Password")
    role_id = fields.Integer(description="Role unique id")
    role = fields.Nested(RoleSchema)
    created_at = fields.DateTime(description="Date of creation")
    updated_at = fields.DateTime(description="Date of modification")
