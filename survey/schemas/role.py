from marshmallow import Schema, fields


class RoleSchema(Schema):
    id = fields.Integer(description="The role unique identifier")
    name = fields.String(description="Name")
