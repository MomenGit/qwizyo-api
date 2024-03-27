#!/usr/bin/env python3
"""Defines Submission Document Model"""
from datetime import datetime, timezone
from wtforms import StringField
from api.models.assignment import Assignment
from api.models.question import Question
from api.models.user import User
from mongoengine import (
    ReferenceField,
    DateTimeField,
    FloatField,
    BooleanField,
    EmbeddedDocument,
    IntField,
    EmbeddedDocumentListField,
    Document
)


class Answer(EmbeddedDocument):
    """Submission Answer Document Model"""
    question = ReferenceField(Question)
    submitted_answer = StringField()
    is_correct = BooleanField()
    points = FloatField()  # For questions other than multiple-choice


class Submission(Document):
    """Assignment Submission Document Model"""
    assignment = ReferenceField(Assignment)
    student = ReferenceField(User)
    answers = EmbeddedDocumentListField(Answer)
    score = FloatField()
    completion_time = IntField()
    submitted_at = DateTimeField()
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
