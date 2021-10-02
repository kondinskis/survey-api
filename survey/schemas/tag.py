from marshmallow import Schema, fields


class TagSchema(Schema):
    id = fields.Integer(description="The tag unique identifier")
    title = fields.String(required=True, description="Tag title")
    description = fields.String(required=True, description="Tag description")
    created_at = fields.DateTime(description="Date of creation")
    updated_at = fields.DateTime(description="Date of modification")
