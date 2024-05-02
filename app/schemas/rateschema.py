from marshmallow import Schema, fields

class RateSchema(Schema):
    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)