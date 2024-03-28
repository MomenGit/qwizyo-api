#!/usr/bin/env python3
"""Define Group Document Model Class"""
from datetime import datetime, timezone
from api.models.assignment import Assignment
from api.models.user import User
from mongoengine import (
    StringField,
    ReferenceField,
    ListField,
    DateTimeField,
    Document
)


class Group(Document):
    """Group Document Model"""
    name = StringField(required=True)
    description = StringField()
    tutor = ReferenceField(User)
    students = ListField(ReferenceField(User))
    assignments = ListField(ReferenceField(Assignment))
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
