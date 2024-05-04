#!/usr/bin/env python3
"""Define submission service functions"""
from datetime import datetime
from api.models.group import Group
from api.models.assignment import Assignment
from api.models.submission import Submission
from api.models.user import User
from api.services.assignment_service import AssignmentService
from api.services.group_service import GroupService
from api.services.quiz_service import QuizService


class SubmissionService:
    """Submission service functions"""

    @staticmethod
    def find_submission_by_id(id) -> Submission:
        """Returns submission by id and tutor
        Args:
            id (string): submission id
        """
        submission = Submission.objects(id=id).first()

        if submission is None:
            raise Exception("Submission not Found")
        if submission.quiz.tutor.id != tutor.id:
            raise Exception("Unauthorized")

        return submission

    @staticmethod
    def find_submissions_of_quiz(quiz_id, tutor):
        """Returns submissions by quiz_id and tutor
        Args:
            quiz_id (string): quiz id
            tutor (user): quiz tutor
        """
        quiz = QuizService.find_quiz_by_id(id=quiz_id, tutor=tutor)
        submissions = Submission.objects(quiz=quiz)

        return submissions

    @staticmethod
    def find_submissions_of_student(student):
        """Returns submissions by student_id and tutor
        Args:
            student (User): student user
        """
        submissions = Submission.objects(student=student)

        return submissions

    @staticmethod
    def find_submissions_of_assignment(assignment_id):
        """Returns submissions by assignment_id
        Args:
            assignment_id (string): assignment id
        """
        assignment = AssignmentService.find_assignment_by_id(id=assignment_id)
        submissions = Submission.objects(assignment=assignment)

        return submissions

    @staticmethod
    def create_submission(quiz_id, tutor, duration, start_at, due_at,
                          groups_ids, students_ids):
        """Creates submission data
        Args:
            quiz_id (str): .
            duration (int): assignment duration
            groups_ids (List(str)): .
            students_ids (List(str)): .
            start_at (str): assignment start date
            due_at (str): assignment due date
        """
        quiz = QuizService.find_quiz_by_id(id=quiz_id, tutor=tutor)

        new_submission = Submission(
            quiz=quiz,
            groups=[Group.objects(id=id).first() for id in groups_ids],
            students=[User.objects(id=id).first() for id in students_ids],
            duration=duration,
            start_at=start_at,
            due_at=due_at
        )

        new_submission.save()
        return new_submission

    @staticmethod
    def update_submission(id, tutor, duration, start_at, due_at,
                          groups_ids, students_ids):
        """Updates submission data
        Args:
            id (str): assignment id
            duration (int): assignment duration
            groups_ids (List(str)): .
            students_ids (List(str)): .
            start_at (str): assignment start date
            due_at (str): assignment due date
        """

        submission = AssignmentService.find_assignment_by_id(id)

        if submission.quiz.id != tutor.id:
            raise Exception("Unauthorized")

        if duration:
            submission.duration = duration
        if start_at:
            submission.start_at = datetime.strptime(
                start_at, "%Y-%m-%d %H:%M:%S")
        if due_at:
            submission.due_at = datetime.strptime(
                due_at, "%Y-%m-%d %H:%M:%S")
        if students_ids:
            submission.students = [User.objects(
                id=id).first() for id in students_ids]
        if groups_ids:
            submission.groups = [Group.objects(
                id=id).first() for id in groups_ids]

        submission.save()

    @staticmethod
    def delete_submission(id, tutor):
        """Delete submission data
        Args:
            id (string): assignment id
            args (dict): data to be updated
        """

        submission = SubmissionService.find_submission_by_id(id)

        if submission.quiz.id != tutor.id:
            raise Exception("Unauthorized")

        submission.delete()
