#!/usr/bin/env python3
"""Defines users service functions"""
from api.models.quiz import Quiz


class QuizService:
    """User service functions"""
    @staticmethod
    def find_user_by_id(id):
        """Returns user by id
        Args:
            id (string): user's id
        """
        pass

    @staticmethod
    def update_user(id, args):
        """Updates user's data
        Args:
            id (string): user's id
            args (dict): data to be updated
        """
        pass
