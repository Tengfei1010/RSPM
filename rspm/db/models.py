from datetime import datetime
from mongoengine import (connect, Document, ListField,
                         StringField, DateTimeField, BooleanField,
                         DictField, ReferenceField, CASCADE)


from rspm.constants import DataBase


mdb = connect(
    db=DataBase.DBNAME,
    host=DataBase.HOST,
    port=DataBase.PORT
)


class Target(Document):
    Host = StringField(unique=True)
    Port = StringField(default='80')
    Created = DateTimeField(default=datetime.now())
    IsValid = BooleanField(default=True)


class Task(Document):
    Target = ReferenceField('Target', reverse_delete_rule=CASCADE)
    Start = DateTimeField()
    End = DateTimeField()
    IsValid = BooleanField(default=True)


class DomainInfo(Document):
    Target = ReferenceField('Target', reverse_delete_rule=CASCADE)
    SubDomains = ListField()
    IsValid = BooleanField(default=True)


class HostInfo(Document):
    # for nmap
    Target = ReferenceField('Target', reverse_delete_rule=CASCADE)
    Ip = StringField()
    Data = DictField()
    IsValid = BooleanField(default=True)


class WebInfo(Document):
    # for whatweb cms
    Target = ReferenceField('Target', reverse_delete_rule=CASCADE)
    Data = DictField()
    IsValid = BooleanField(default=True)
