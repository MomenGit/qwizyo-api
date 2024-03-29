#!/usr/bin/env python3
"""Define User Resource for User Routes Handling
"""
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from api.common.decorators import role_required
from api.services.quiz_service import QuizService


class Quiz(Resource):
    """User Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor')
    def get(self, id, user):
        """Retrieve details of a specific quiz"""
        pass

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def put(self, id):
        """Update quiz details"""
        pass

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def delete(self, id):
        """Delete a quiz"""
        pass


class QuizList(Resource):
    """User Resource Route Handler"""

    @jwt_required(optional=False)
    @role_required('tutor')
    def get(self, user):
        """Retrieve a list of quizzes created by the current user (tutor)"""
        pass

    @jwt_required(optional=False, fresh=True)
    @role_required('tutor')
    def post(self, user):
        """Create a new quiz"""
        pass
