#!/usr/bin/env python3
"""Define Quiz Document Model Class"""
from datetime import datetime, timezone
from api.models.question import Question
from mongoengine import (
    StringField, EmbeddedDocumentListField,
    Document, DateTimeField,  ReferenceField)
from api.models.user import User


class Quiz(Document):
    """Quiz Document Model"""
    title = StringField(required=True)
    description = StringField(required=True)
    questions = EmbeddedDocumentListField(Question)
    tutor = ReferenceField(User, db_field="tutor_id")
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    meta = {"collection": "quizzes"}
