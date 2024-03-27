#!/usr/bin/env python3
"""
"""
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from api.models.user import User as UserModel
from api.services.users_service import find_user_by_id, update_user


class User(Resource):
    """User Resource Route Handler"""
    parser = reqparse.RequestParser()

    parser.add_argument(
        "email", type=str, required=False, help="This field cannot be blank."
    )
    parser.add_argument(
        "first_name", type=str, required=False, help="This field cannot be blank."
    )
    parser.add_argument(
        "last_name", type=str, required=False, help="This field cannot be blank."
    )

    @jwt_required(optional=False)
    def get(self, id):
        """"""
        user_id = get_jwt_identity() if id == "me" else id

        result = find_user_by_id(user_id)

        if not isinstance(result, UserModel):
            return result

        user_dict = {
            "id": str(result.id),
            "username": result.username,
            "first_name": result.first_name,
            "last_name": result.last_name
        }

        if id == "me":
            user_dict['email'] = result.email

        return user_dict, 200

    @jwt_required(optional=False, fresh=True)
    def put(self, id):
        """"""
        pass
