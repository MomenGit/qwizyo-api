#!/usr/bin/env python3
"""Defines authentication service functions"""
from flask_jwt_extended import (
    create_access_token, get_jwt_identity, create_refresh_token)
from werkzeug.security import check_password_hash, generate_password_hash
from api.models.user import User
from datetime import datetime, timezone


def generate_non_fresh_access_token():
    """Generates a non-fresh access token using refresh token
    Returns:
        New non-fresh access token
    """
    # retrive the user's identity from the refresh token
    # using a Flask-JWT-Extended built-in method
    current_user = get_jwt_identity()
    # return a non-fresh token for the user
    new_token = create_access_token(identity=current_user, fresh=False)
    return new_token


def authenticate(username, password):
    """Authenticate user on login request
    Args:
        username (string): user's username
        password (string): user's plain text password
    Returns:
        - On success: new access and refresh tokens
        - Otherwise: None
    """
    user = User.objects(username=username).first()
    if user and check_password_hash(user.password, password):
        # when authenticated, return a fresh access token and a refresh token
        access_token = create_access_token(
            identity=str(user.id), fresh=True)
        refresh_token = create_refresh_token(str(user.id))
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
    else:
        return None


def register_user(data):
    """Register new user
    Args:
        Data (dict): User's registered data
    Returns:
        - On success: new user, 201 created status code
        - Otherwise: error message, 409 conflict status code
    """
    retrieve_username = User.objects(username=data["username"])
    if retrieve_username:
        return {"message": "The username already exist"}, 409

    retrieve_email = User.objects(email=data["email"])
    if retrieve_email:
        return {"message": "The email already exist"}, 409

    password: str = data["password"]
    if len(password) < 7:
        return {"message": "The password is too short"}, 409
    if len(password) > 14:
        return {"message": "The password is too long"}, 409
    if not password.isalnum():
        return {
            "message":
            "The password can not contain non-alphanumeric characters"
        }, 409

    new_user = User(
        username=data["username"],
        email=data["email"],
        password=generate_password_hash(password),
        role=data["role"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        created_at=datetime.now(tz=timezone.utc),
        updated_at=datetime.now(tz=timezone.utc),
    )
    new_user.save()
    del new_user.password
    return new_user.to_json(), 200
