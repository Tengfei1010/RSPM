from mongoengine import (Document,
                         StringField, ObjectIdField,
                         DateTimeField, BooleanField,
                         DictField)


class Task(Document):
    Id = ObjectIdField()
    Host = StringField()
    Status = StringField()
    Start = DateTimeField()
    End = DateTimeField()
    IsValid = BooleanField()
    Data = DictField()
