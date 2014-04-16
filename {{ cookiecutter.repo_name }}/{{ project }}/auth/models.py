from motorengine.document import Document
from motorengine import fields


class User(Document):
    name = fields.StringField(required=True)
    email = fields.EmailField(required=True)
