#!/usr/bin/env python3
""""""
from api import db
from api.models.group import Group
from api.models.quiz import Quiz
from mongoengine import ReferenceField, DateTimeField, ListField, IntField

from api.models.user import User


class Assignment(Document):
    """"""
    quiz = ReferenceField(Quiz)
    groups = ListField(ReferenceField(Group))
    students = ListField(ReferenceField(User))
    start_at = DateTimeField(required=True)
    due_at = DateTimeField(required=True)
    duration = IntField()  # Minutes
    created_at = DateTimeField()
    updated_at = DateTimeField()
