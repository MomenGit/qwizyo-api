#!/usr/bin/env python3
"""Defines users service functions"""
from api.models.user import User


class UserService:
    """User service functions"""
    @staticmethod
    def find_user_by_id(id):
        """Returns user by id
        Args:
            id (string): user's id
        """
        if len(id) != 24:
            return {"message": "Invalid User's ID"}, 402

        user = User.objects(id=id).first()
        if user is None:
            return {"message": "User not found"}, 404

        return user

    @staticmethod
    def update_user(id, args):
        """Updates user's data
        Args:
            id (string): user's id
            args (dict): data to be updated
        """
        result = find_user_by_id(id)

        if not isinstance(result, User):
            return result

        user = result

        updatable_fields = ['email', 'first_name', 'last_name']
        # Update user information
        for field in updatable_fields:
            arg = args.get(field)
            if arg:
                user.__setattr__(field, arg)

        # Save updated user to database
        user.save()

        return {'message': 'User updated successfully'}, 200
