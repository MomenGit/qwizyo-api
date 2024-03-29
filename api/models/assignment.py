#!/usr/bin/env python3
"""Define Assignment Document Model Class"""
from datetime import datetime, timezone
from api.models.quiz import Quiz
from mongoengine import (
    ReferenceField,
    DateTimeField,
    ListField,
    IntField,
    Document
)
from api.models.user import User


class Assignment(Document):
    """Assignment Document Model"""
    quiz = ReferenceField(Quiz, db_field="quiz_id")
    groups = ListField(ReferenceField('Group'), db_field="groups_ids")
    students = ListField(ReferenceField(User), db_field="students_ids")
    start_at = DateTimeField()
    due_at = DateTimeField()
    duration = IntField()  # Minutes
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    meta = {"collection": "assignments"}
