#!/usr/bin/env python3
""""""
from datetime import datetime, timezone
from api.models.question import Question
from mongoengine import (
    StringField, EmbeddedDocumentListField,
    Document, DateTimeField,  ReferenceField)
from api.models.user import User


class Quiz(Document):
    """"""
    title = StringField(required=True)
    description = StringField(required=True)
    questions = EmbeddedDocumentListField(Question)
    tutor = ReferenceField(User)
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
