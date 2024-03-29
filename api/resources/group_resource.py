#!/usr/bin/env python3
"""Defines Group Resource for Group Routes Handling
"""
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from api.common.decorators import role_required
from api.services.group_service import GroupService


class Group(Resource):
    """Group Resource Route Handler"""

    @jwt_required(optional=False)
    def get(self, id):
        """Returns group's data"""
        try:
            group = GroupService.find_group_by_id(id)
        except Exception as err:
            return {"message": str(err)}, 404

        return {
            "title": group.title,
            "description": group.description,
            "students": group.students,
            "assignments": group.assignments
        }

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def put(self, id, user):
        """Updates group's profile"""
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str)
        parser.add_argument("description", type=str)
        parser.add_argument("assignments", type=str)
        parser.add_argument("students", type=str)
        args = parser.parse_args()

        try:
            GroupService.update_group(id, user, args)
        except Exception as err:
            return {"message": str(err)}, 404

        return {"message": "Group has been updated successfully"}, 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def delete(self, id, tutor):
        """Updates group's profile"""
        try:
            GroupService.delete_group(id=id, tutor=tutor)
        except Exception as err:
            return {"message": str(err)}, 404

        return {"message": "Group has been deleted successfully"}, 200


class Groups(Resource):
    """Group Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor', 'student')
    def get(self, user):
        """Returns groups List"""
        return [
            {
                "id": str(group.id),
                "title": group.title,
                "description": group.description,
                "tutor": str(group.tutor)
            } for group in GroupService.find_groups(user)], 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def post(self, user):
        """Creates new group"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title", type=str, required=True, help="This field cannot be blank.")
        parser.add_argument(
            "description", type=str, required=True, help="This field cannot be blank."
        )
        args = parser.parse_args()
        new_group = GroupService.create_group(user, args)
        if new_group is None:
            return {"message": "Group with the same title exists"}, 409

        return {
            "id": str(new_group.id),
            "title": new_group.title,
            "description": new_group.description
        }, 201
