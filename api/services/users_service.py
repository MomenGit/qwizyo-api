#!/usr/bin/env python3
"""Defines users service functions"""
from unittest import result
from api.models.user import User


def find_user_by_id(id):
    """Returns user by id"""
    if len(id) != 24:
        return {"message": "Invalid User's ID"}, 402

    user = User.objects(id=id).first()
    if user is None:
        return {"message": "User not found"}, 404

    return user


def update_user(id, data):
    """"""
    result = find_user_by_id(id)

    if not isinstance(result, User):
        return result
