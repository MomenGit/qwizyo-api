#!/usr/bin/env python3
"""Define assignment service functions"""
from datetime import datetime
from api.models.group import Group
from api.models.assignment import Assignment
from api.models.user import User
from api.services.group_service import GroupService
from api.services.quiz_service import QuizService


class AssignmentService:
    """Assignment service functions"""

    @staticmethod
    def find_assignment_by_id(id) -> Assignment:
        """Returns assignment by id and tutor
        Args:
            id (string): assignment id
            tutor (user): assignment tutor
        """
        assignment = Assignment.objects(id=id).first()

        if assignment is None:
            raise Exception("Assignment not Found")
        if assignment.quiz.tutor.id != tutor.id:
            raise Exception("Unauthorized")

        return assignment

    @staticmethod
    def find_assignments_of_quiz(quiz_id, tutor):
        """Returns assignment by quiz_id and tutor
        Args:
            id (string): quiz id
            tutor (user): quiz tutor
        """
        quiz = QuizService.find_quiz_by_id(quiz_id, tutor=tutor)
        assignments = Assignment.objects(quiz=quiz)

        return assignments

    @staticmethod
    def find_assignments_of_student(student):
        """Returns assignment by quiz_id and tutor
        Args:
            student (User): student user
        """
        assignments = Assignment.objects(students=student)

        return assignments

    @staticmethod
    def find_assignments_of_group(group_id):
        """Returns assignments by group_id
        Args:
            group_id (string): group id
        """
        group = GroupService.find_group_by_id(group_id)
        assignments = Assignment.objects(groups=group)

        return assignments

    @staticmethod
    def create_assignment(quiz_id, tutor, duration, start_at, due_at,
                          groups_ids, students_ids):
        """Creates assignment data
        Args:
            quiz_id (str): .
            duration (int): assignment duration
            groups_ids (List(str)): .
            students_ids (List(str)): .
            start_at (str): assignment start date
            due_at (str): assignment due date
        """
        quiz = QuizService.find_quiz_by_id(id=quiz_id, tutor=tutor)

        new_assignment = Assignment(
            quiz=quiz,
            groups=[Group.objects(id=id).first() for id in groups_ids],
            students=[User.objects(id=id).first() for id in students_ids],
            duration=duration,
            start_at=start_at,
            due_at=due_at
        )

        new_assignment.save()
        return new_assignment

    @staticmethod
    def update_assignment(id, tutor, duration, start_at, due_at,
                          groups_ids, students_ids):
        """Updates assignment data
        Args:
            id (str): assignment id
            duration (int): assignment duration
            groups_ids (List(str)): .
            students_ids (List(str)): .
            start_at (str): assignment start date
            due_at (str): assignment due date
        """

        assignment = AssignmentService.find_assignment_by_id(id)

        assignment.select_related()

        if assignment.quiz.id != tutor.id:
            raise Exception("Unauthorized")

        if duration:
            assignment.duration = duration
        if start_at:
            assignment.start_at = datetime.strptime(
                start_at, "%Y-%m-%d %H:%M:%S")
        if due_at:
            assignment.due_at = datetime.strptime(
                due_at, "%Y-%m-%d %H:%M:%S")
        if students_ids:
            assignment.students = [User.objects(
                id=id).first() for id in students_ids]
        if groups_ids:
            assignment.groups = [Group.objects(
                id=id).first() for id in groups_ids]

        assignment.save()

    @staticmethod
    def delete_assignment(id, tutor):
        """Delete assignment data
        Args:
            id (string): assignment id
            args (dict): data to be updated
        """

        assignment = AssignmentService.find_assignment_by_id(id)
        assignment.select_related()

        if assignment.quiz.id != tutor.id:
            raise Exception("Unauthorized")

        assignment.delete()
