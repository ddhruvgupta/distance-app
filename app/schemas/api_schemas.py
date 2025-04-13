from marshmallow import Schema, fields

class DistanceRequestSchema(Schema):
    address1 = fields.Str(required=True, description="First address")
    address2 = fields.Str(required=True, description="Second address")

class DistanceResponseSchema(Schema):
    distance = fields.Float(description="Distance in miles")

class HistoryResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    address1 = fields.Str()
    address2 = fields.Str()
    distance = fields.Float()
    created_at = fields.DateTime()

class PaginatedHistoryResponseSchema(Schema):
    page = fields.Int()
    page_size = fields.Int()
    total_count = fields.Int()
    total_pages = fields.Int()
    results = fields.List(fields.Nested(HistoryResponseSchema))