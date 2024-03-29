#!/usr/bin/env python3
"""Defines users service functions"""
from api.models.question import Question
from api.models.quiz import Quiz


class QuizService:
    """Quiz service functions"""

    @staticmethod
    def find_quiz_by_id(id, tutor) -> Quiz:
        """Returns quiz by id and tutor
        Args:
            id (string): quiz id
            tutor (user): quiz tutor
        """
        quiz = Quiz.objects(id=id, tutor=tutor).first()
        if quiz is None:
            raise Exception("Quiz not Found")
        return quiz

    @staticmethod
    def find_quizzes(tutor):
        """Returns quiz by id and tutor
        Args:
            id (string): quiz id
            tutor (user): quiz tutor
        """
        quizzes = Quiz.objects(tutor=tutor)
        return quizzes

    @staticmethod
    def create_quiz(tutor, title, questions, description):
        """Updates quiz data
        Args:
            id (string): quiz id
            args (dict): data to be updated
        """
        new_quiz = Quiz(
            tutor=tutor, title=title, description=description
        )
        for question in questions:
            try:
                new_question = Question(
                    type=question['type'],
                    question=question['question'],
                    correct_answer=question['correct_answer'],
                    points=question['points']
                )
                if question.get('options'):
                    new_question.options = question['options']
                new_quiz.questions.append(new_question)
            except Exception as err:
                raise err
        new_quiz.save()
        return new_quiz

    @staticmethod
    def update_quiz(id, tutor, args):
        """Updates quiz data
        Args:
            id (string): quiz id
            args (dict): data to be updated
        """
        try:
            quiz = QuizService.find_quiz_by_id(id, tutor)
        except Exception as e:
            raise e

    @staticmethod
    def delete_quiz(id, tutor):
        """Updates quiz data
        Args:
            id (string): quiz id
            args (dict): data to be updated
        """
        try:
            quiz = QuizService.find_quiz_by_id(id, tutor)
        except Exception as e:
            raise e

        quiz.delete()
