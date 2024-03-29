#!/usr/bin/env python3
"""Defines users service functions"""
from api.models.group import Group


class GroupService:
    """Group service functions"""
    @staticmethod
    def find_groups(user):
        """Find groups for a student or a tutor"""
        if user.role == 'tutor':
            groups = Group.objects(tutor=user)
        else:
            groups = Group.objects(students=user)

        return groups

    @staticmethod
    def find_group_by_id(id):
        """Find groups for a student or a tutor"""
        group: Group = Group.objects(id=id).first()
        if group is None:
            raise Exception("Group not found")

        return group

    @staticmethod
    def create_group(tutor, args):
        """Creates new group
        Args:
            tutor (Tutor): tutor of the group
            args (dict): group data
        """
        existing = Group.objects(title=args.get('title'), tutor=tutor).first()

        if existing:
            raise Exception("Group already exists")

        group = Group(
            title=args.get('title'),
            description=args.get('description'),
            tutor=tutor,
        )
        group.save()
        return group

    @staticmethod
    def update_group(id, tutor, args):
        """"""
        """Updates group's data
        Args:
            id (string): group's id
            tutor (Tutor): group's tutor
            args (dict): data to be updated
        """
        group = Group.objects(id=id, tutor=tutor).first()

        if group is None:
            raise Exception("Group not found")

        # Update group fields
        if 'title' in args:
            group.title = args['title']
        if 'description' in args:
            group.description = args['description']

        # Save updated user to database
        group.save()

    @staticmethod
    def delete_group(id, tutor):
        """Deletes group from database
        Args:
            id (string): group's id
            tutor (Tutor): group's tutor
        """
        group: Group = Group.objects(id=id, tutor=tutor).first()

        if group:
            group.delete()
        else:
            raise Exception("Group not found")
