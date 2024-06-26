#!/usr/bin/env python3
"""Define Quiz Resource for Quiz Routes Handling
"""
import json
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from api.common.decorators import role_required
from api.services.quiz_service import QuizService


class Quiz(Resource):
    """Quiz Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor')
    def get(self, id, user):
        """Retrieve details of a specific quiz"""
        try:
            quiz = QuizService.find_quiz_by_id(id, tutor=user)
        except Exception as err:
            return {"message": str(err)}, 404

        return json.loads(quiz.to_json()), 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def put(self, id, user):
        """Update quiz details"""
        parser = reqparse.RequestParser()

        parser.add_argument(
            "title", type=str, required=False, help="This field cannot be blank."
        )
        parser.add_argument("description", type=str, required=False)
        parser.add_argument(
            "questions", type=list, required=False, help="This field cannot be blank.",
            location='json'
        )
        args = parser.parse_args()

        try:
            QuizService.update_quiz(
                id=id,
                tutor=user,
                title=args.get('title'),
                description=args.get('description'),
                questions=args.get('questions')
            )
        except Exception as err:
            return {"message": str(err)}, 409

        return {"message": "Quiz has been updated successfully"}, 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def delete(self, id, user):
        """Delete a quiz"""
        try:
            QuizService.delete_quiz(id, tutor=user)
        except Exception as err:
            return {"message": str(err)}, 404

        return {"message": "Quiz has been deleted successfully"}, 200


class QuizList(Resource):
    """User Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor')
    def get(self, user):
        """Retrieve a list of quizzes created by the current user (tutor)"""
        quizzes = QuizService.find_quizzes(tutor=user)
        return [json.loads(quiz.to_json()) for quiz in quizzes], 200

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def post(self, user):
        """Create a new quiz"""
        parser = reqparse.RequestParser()

        parser.add_argument(
            "title", type=str, required=True, help="This field cannot be blank."
        )
        parser.add_argument("description", type=str, required=False)
        parser.add_argument(
            "questions", type=list, required=True, help="This field cannot be blank.",
            location='json'
        )
        args = parser.parse_args()

        try:
            quiz = QuizService.create_quiz(
                tutor=user,
                title=args.get('title'),
                description=args.get('description'),
                questions=args.get('questions')
            )
        except Exception as err:
            return {"message": str(err)}, 409

        return json.loads(quiz.to_json()), 201
