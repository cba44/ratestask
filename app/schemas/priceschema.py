from marshmallow import Schema, fields

class PriceSchema(Schema):
    day = fields.Str(dump_only=True)
    average_price = fields.Int(dump_only=True)