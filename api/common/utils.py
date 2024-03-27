#!/usr/bin/env python3
"""Define utils functions"""
from api.resources import (
    auth_resource,
    group_resource,
    user_resource,
    miscellaneous_resource
)


def setup_routes(api):
    """Map Resources to routes"""
    api.add_resource(user_resource.User, '/users/<string:id>')
    api.add_resource(auth_resource.RegisterAuth, '/auth/register')
    api.add_resource(auth_resource.LoginAuth, '/auth/login')
    api.add_resource(auth_resource.TokenRefresh, '/auth/refresh')
    api.add_resource(miscellaneous_resource.Status, '/ping')
    api.add_resource(group_resource.Groups, '/groups')
    api.add_resource(group_resource.Group, '/groups/<string:id>')
    """ api.add_resource('/quizzes')
    api.add_resource('/quizzes/<str:id>')
    api.add_resource('/assignments')
    api.add_resource('/assignments/<str:id>') """
