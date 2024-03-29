#!/usr/bin/env python3
"""Define Question Embedded Document Model Class"""
from datetime import datetime, timezone
from bson import ObjectId
from mongoengine import (
    EmbeddedDocument,
    StringField,
    DateTimeField,
    ListField,
    FloatField,
    ObjectIdField
)


class Question(EmbeddedDocument):
    """Question Embedded Document Model"""
    id = ObjectIdField(db_field='_id',  unique=True,
                       primary_key=True, default=ObjectId())
    type = StringField(
        required=True, choices=['multiple-choice', 'short-answer', 'long-answer'])
    question = StringField(required=True)
    options = ListField(StringField())  # for multiple-choice questions
    correct_answer = StringField(required=True)
    points = FloatField(required=True)
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    meta = {"collection": "questions"}
