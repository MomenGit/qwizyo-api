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
    quiz = ReferenceField(Quiz)
    groups = ListField(ReferenceField('Group'))
    students = ListField(ReferenceField(User))
    start_at = DateTimeField(required=True)
    due_at = DateTimeField(required=True)
    duration = IntField()  # Minutes
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
