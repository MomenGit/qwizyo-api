#!/usr/bin/env python3
""""""
from mongoengine import StringField, EmailField, DateTimeField, Document


class User(Document):
    """"""
    username = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    role = StringField(required=True, choices=[
                       'tutor', 'student'])  # "tutor" or "student"
    created_at = DateTimeField()
    updated_at = DateTimeField()
