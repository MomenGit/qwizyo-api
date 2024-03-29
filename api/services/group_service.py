#!/usr/bin/env python3
"""Defines users service functions"""
from api.models.assignment import Assignment
from api.models.group import Group
from api.models.user import User


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

        return group

    @staticmethod
    def create_group(tutor, args):
        """Creates new group
        Args:
            tutor (Tutor): tutor of the group
            args (dict): group data
        """
        existing = Group.objects(name=args.get('name'), tutor=tutor)
        if existing:
            raise Exception("Group already exists")
        group = Group(
            name=args.get('name'),
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

        if not isinstance(group, Group):
            raise Exception("Group not found")

        # Update group fields
        if 'name' in args:
            group.title = args['name']
        if 'description' in args:
            group.description = args['description']

        # Save updated user to database
        group.save()

        return True

    @staticmethod
    def update_group_assignments(id, tutor, assignment_id, operation):
        """Updates group's data
        Args:
            id (string): group's id
            tutor (Tutor): group's tutor
            args (dict): data to be updated
        """
        group = Group.objects(id=id, tutor=tutor).first()

        if not isinstance(group, Group):
            raise Exception("Group not found")

        assignment = Assignment.objects(id=assignment_id).first()
        if not isinstance(assignment, Assignment):
            raise Exception("Assignment not found")

        if operation == "add":
            group.assignments.append(assignment)
        elif operation == "remove":
            group.assignments.remove(assignment)
        else:
            raise Exception("Operation is not allowed")

        # Save updated user to database
        group.save()

    @staticmethod
    def update_group_students(id, tutor, student_id, operation):
        """Updates group's data
        Args:
            id (string): group's id
            tutor (Tutor): group's tutor
            args (dict): data to be updated
        """
        group = Group.objects(id=id, tutor=tutor).first()

        if not isinstance(group, Group):
            raise Exception("Group not found")

        student = User.objects(id=student_id).first()
        if not isinstance(student, User):
            raise Exception("Student not found")

        if operation == "add":
            group.students.append(student)
        elif operation == "remove":
            group.students.remove(student)
        else:
            raise Exception("Operation is not allowed")

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
