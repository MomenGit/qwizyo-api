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
    title = StringField(required=True)
    description = StringField()
    tutor = ReferenceField(User, db_field="tutor_id")
    students = ListField(ReferenceField(User), db_field="students_ids")
    assignments = ListField(ReferenceField(Assignment),
                            db_field="assignments_ids")
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    meta = {"collection": "groups"}
