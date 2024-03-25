#!/usr/bin/env python3
""""""
from datetime import datetime, timezone
from api.models.user import User
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash


class RegisterAuth(Resource):
    """"""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "email", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "first_name", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "last_name", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "role", type=str, required=True, help="This field cannot be blank."
    )

    def post(self):
        """"""
        data = self.parser.parse_args()

        new_user = User(
            username=data["username"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
            role=data["role"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            created_at=datetime.now(tz=timezone.utc),
            updated_at=datetime.now(tz=timezone.utc),
        )
        new_user.save()
        return new_user.to_json(), 201


class LoginAuth(Resource):
    """"""

    # defining the request parser and expected arguments in the request
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    def get(self):
        """"""
        data = self.parser.parse_args()
        # read from database to find the user and then check the password
        user = User.objects(username=data["username"]).first()
        if user and check_password_hash(user.password, data['password']):
            # when authenticated, return a fresh access token and a refresh token
            access_token = create_access_token(
                identity=str(user.id), fresh=True)
            refresh_token = create_refresh_token(str(user.id))
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {"message": "Invalid Credentials!"}, 401


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def get(self):
        # retrive the user's identity from the refresh token using a Flask-JWT-Extended built-in method
        current_user = get_jwt_identity()
        # return a non-fresh token for the user
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
