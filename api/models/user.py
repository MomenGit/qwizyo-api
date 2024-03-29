#!/usr/bin/env python3
"""Define User Document Model Class"""
from datetime import datetime, timezone
from mongoengine import StringField, EmailField, DateTimeField, Document


class User(Document):
    """User Document Model"""
    username = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    role = StringField(required=True, choices=[
                       'tutor', 'student'])  # "tutor" or "student"
    created_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    updated_at = DateTimeField(default=datetime.now(tz=timezone.utc))
    meta = {"collection": "users"}
