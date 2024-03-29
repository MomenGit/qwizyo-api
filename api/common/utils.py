#!/usr/bin/env python3
"""Define utils functions"""
from api.resources import (
    assignment_resource,
    auth_resource,
    group_resource,
    quiz_resource,
    user_resource,
    miscellaneous_resource
)


def setup_routes(api):
    """Map Resources to routes"""
    api.add_resource(user_resource.User, '/users/<string:id>')

    # Auth Routes
    api.add_resource(auth_resource.RegisterAuth, '/auth/register')
    api.add_resource(auth_resource.LoginAuth, '/auth/login')
    api.add_resource(auth_resource.TokenRefresh, '/auth/refresh')

    # Status Route
    api.add_resource(miscellaneous_resource.Status, '/ping')

    # Group Routes
    api.add_resource(group_resource.Groups, '/groups')
    api.add_resource(group_resource.Group, '/groups/<string:id>')

    # Quiz Routes
    api.add_resource(quiz_resource.QuizList, '/quizzes')
    api.add_resource(quiz_resource.Quiz, '/quizzes/<string:id>')

    # Assignment Routes
    api.add_resource(assignment_resource.AssignmentList, '/assignments')
    api.add_resource(assignment_resource.Assignment,
                     '/assignments/<string:id>')
    api.add_resource(assignment_resource.QuizAssignmentsList,
                     '/quizzes/<string:id>/assignments')
    api.add_resource(assignment_resource.GroupAssignmentsList,
                     '/groups/<string:id>/assignments')
