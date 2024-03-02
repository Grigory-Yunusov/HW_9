from mongoengine import StringField, Document, ObjectIdField, ReferenceField, ListField
import uuid

class Author(Document):
    # id = StringField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField(max_length=4000)
    meta = {'indexes':['born_date', 'born_location']}


class Quote(Document):
    # id = StringField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    tags = ListField(StringField(max_length=50))
    quote = StringField(max_length=1050)

    author = ReferenceField(Author)
