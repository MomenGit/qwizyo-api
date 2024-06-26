#!/usr/bin/env python3
"""Defines Auth Resources for Auth Routes Handling"""
import json
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
)
from api.services.auth_service import AuthService


class RegisterAuth(Resource):
    """Registration Resource Route Handler"""
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
        """Register new User to the database"""
        data = self.parser.parse_args()
        try:
            new_user = AuthService.register_user(data)
        except Exception as err:
            return err.args[0], err.args[1]

        return json.loads(new_user), 200


class LoginAuth(Resource):
    """Login Resource Route Handler"""
    # defining the request parser and expected arguments in the request
    parser = reqparse.RequestParser()

    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be blank."
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank."
    )

    def get(self):
        """Auth User Through Login
        Return:
            JWT {access token + refresh token}
        """
        data = self.parser.parse_args()
        # read from database to find the user and then check the password

        result = AuthService.authenticate(data['username'], data['password'])
        if result is not None:
            return result

        return {"message": "Invalid Credentials!"}, 401


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def get(self):
        """Refresh JWT Access Token
        Returns:
            A non-fresh JWT Access Token
        """
        new_token = AuthService.generate_non_fresh_access_token()
        return {"access_token": new_token}, 200
