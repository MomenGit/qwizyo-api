#!/usr/bin/env python3
""""""
from api.models.assignment import Assignment
from api.models.user import User
from mongoengine import StringField, ReferenceField, ListField
from mongoengine import DateTimeField, Document


class Group(Document):
    """"""
    name = StringField(required=True)
    description = StringField()
    tutor = ReferenceField(User)
    students = ListField(ReferenceField(User))
    assignments = ListField(ReferenceField(Assignment))
    created_at = DateTimeField()
    updated_at = DateTimeField()
