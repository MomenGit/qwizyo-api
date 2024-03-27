#!/usr/bin/env python3
"""Define decorator functions"""
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from api.models.user import User


def role_required(*roles):
    """Decorator function that requires certain role for authorization"""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            # Get current user ID from JWT token
            current_user_id = get_jwt_identity()

            # Retrieve current user from database
            user = User.objects(id=current_user_id).first()

            if not user:
                return {'message': 'User not found'}, 404
            # Check if the user has the required role
            if user.role not in roles:
                return {'message': 'Unauthorized access'}, 403
            # Call the wrapped view function
            return view_func(user=user, *args, **kwargs)

        return wrapper

    return decorator
