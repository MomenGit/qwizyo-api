#!/usr/bin/env python3
"""Defines Group Resource for Group Routes Handling
"""
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from api.common.decorators import role_required
from api.services.groups_service import create_group, find_groups


class Group(Resource):
    """Group Resource Route Handler"""

    @jwt_required(optional=False)
    def get(self, id):
        """Returns group's data"""

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def put(self, id):
        """Updates group's profile"""

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def delete(self, id):
        """Updates group's profile"""


class Groups(Resource):
    """Group Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor', 'student')
    def get(self, user):
        """Returns groups List"""
        return [
            {
                "id": str(group.id),
                "name": group.name,
                "description": group.description,
                "tutor": str(group.tutor)
            } for group in find_groups(user)], 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def post(self, user):
        """Creates new group"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "name", type=str, required=True, help="This field cannot be blank.")
        parser.add_argument(
            "description", type=str, required=True, help="This field cannot be blank."
        )
        args = parser.parse_args()
        new_group = create_group(user, args)
        if new_group is None:
            return {"message": "Group with the same name exists"}, 409

        return {
            "id": str(new_group.id),
            "name": new_group.name,
            "description": new_group.description
        }, 201
