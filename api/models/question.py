#!/usr/bin/env python3
""""""
from mongoengine import EmbeddedDocument, StringField, DateTimeField
from mongoengine import ListField, FloatField


class Question(EmbeddedDocument):
    """"""
    type = StringField(
        required=True, choices=['multiple-choice', 'short-answer', 'long-answer'])
    question = StringField(required=True)
    options = ListField(StringField)  # for multiple-choice questions
    correct_answer = StringField(required=True)
    points = FloatField(required=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()
