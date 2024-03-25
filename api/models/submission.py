#!/usr/bin/env python3
""""""
from wtforms import StringField
from api.models.assignment import Assignment
from api.models.user import User
from mongoengine import ReferenceField, DateTimeField, FloatField, BooleanField
from mongoengine import EmbeddedDocument, IntField, EmbeddedDocumentListField
from mongoengine import Document


class Answer(EmbeddedDocument):
    """"""
    submitted_answer = StringField()
    is_correct = BooleanField()
    points = FloatField()  # For questions other than multiple-choice


class Submission(Document):
    """"""
    assignment = ReferenceField(Assignment)
    student = ReferenceField(User)
    answers = EmbeddedDocumentListField(Answer)
    score = FloatField()
    completion_time = IntField()
    submitted_at = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
