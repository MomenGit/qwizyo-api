#!/usr/bin/env python3
""""""
from api.models.question import Question
from mongoengine import StringField, EmbeddedDocumentListField, Document
from mongoengine import DateTimeField,  ReferenceField
from api.models.user import User


class Quiz(Document):
    """"""
    title = StringField(required=True)
    description = StringField(required=True)
    questions = EmbeddedDocumentListField(Question)
    tutor = ReferenceField(User)
    created_at = DateTimeField()
    updated_at = DateTimeField()
