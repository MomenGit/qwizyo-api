#!/usr/bin/env python3
"""Define Assignment Resource for Assignment Routes Handling
"""
import json
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from api.common.decorators import role_required
from api.services.assignment_service import AssignmentService
from api.services.quiz_service import QuizService


class Assignment(Resource):
    """Assignment Resource Route Handler"""

    @jwt_required(optional=False)
    def get(self, id):
        """Retrieve details of a specific assignment"""
        try:
            assignment = AssignmentService.find_assignment_by_id(id)
        except Exception as err:
            return {"message": str(err)}, 404

        return json.loads(assignment.to_json()), 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def put(self, id, user):
        """Update assignment details"""
        parser = reqparse.RequestParser()

        parser.add_argument("duration", type=int, required=False)
        parser.add_argument("start_at", type=str, required=False)
        parser.add_argument("due_at", type=str, required=False)
        parser.add_argument("groups_ids", type=list,
                            required=False, location='json')
        parser.add_argument("students_ids", type=list,
                            required=False, location='json')
        args = parser.parse_args()

        try:
            AssignmentService.update_assignment(
                id=id,
                tutor=user,
                duration=args.get('duration'),
                start_at=args.get('start_at'),
                due_at=args.get('due_at'),
                groups_ids=args.get('groups_ids'),
                students_ids=args.get('students_ids')
            )
        except Exception as err:
            return {"message": str(err)}, 409

        return {"message": "Assignment has been updated successfully"}, 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def delete(self, id, user):
        """Delete an assignment"""
        try:
            AssignmentService.delete_assignment(id, tutor=user)
        except Exception as err:
            return {"message": str(err)}, 404

        return {"message": "Assignment has been deleted successfully"}, 200


class AssignmentList(Resource):
    """Assignments List Resource Route Handler"""
    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def post(self, user):
        """Create a new assignment"""
        parser = reqparse.RequestParser()

        parser.add_argument("duration", type=int, required=False)
        parser.add_argument("start_at", type=str, required=False)
        parser.add_argument("due_at", type=str, required=False)
        parser.add_argument("groups_ids", type=list,
                            required=False, location='json')
        parser.add_argument("students_ids", type=list,
                            required=False, location='json')
        args = parser.parse_args()
        args = parser.parse_args()

        try:
            assignment = AssignmentService.create_assignment(
                quiz_id=id,
                duration=args.get('duration'),
                start_at=args.get('start_at'),
                due_at=args.get('due_at'),
                groups_ids=args.get('groups_ids'),
                students_ids=args.get('students_ids')
            )
        except Exception as err:
            return {"message": str(err)}, 409

        return json.loads(assignment.to_json()), 201


class StudentAssignmentsList(Resource):
    """Assignments List Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('student')
    def get(self, id, user):
        """Retrieve assignments of a specific group"""
        try:
            assignments = AssignmentService.find_assignments_of_student(
                student_id=id)
        except Exception as err:
            return {"message": str(err)}, 404

        return [json.loads(assignment.to_json())for assignment in assignments], 200


class GroupAssignmentsList(Resource):
    """Assignments List Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor', 'student')
    def get(self, id, user):
        """Retrieve assignments of a specific group"""
        try:
            assignments = AssignmentService.find_assignments_of_group(
                group_id=id)
        except Exception as err:
            return {"message": str(err)}, 404

        return [json.loads(assignment.to_json())for assignment in assignments], 200


class QuizAssignmentsList(Resource):
    """Assignments List Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor')
    def get(self, id, user):
        """Retrieve assignments of a specific quiz"""
        try:
            assignments = AssignmentService.find_assignments_of_quiz(
                quiz_id=id, tutor=user)
        except Exception as err:
            return {"message": str(err)}, 404

        return [json.loads(assignment.to_json())for assignment in assignments], 200
