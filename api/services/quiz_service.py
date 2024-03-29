#!/usr/bin/env python3
"""Defines users service functions"""
from bson import ObjectId
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
            tutor (user): quiz tutor
            title (str): quiz title
            questions (List(dict)): quiz questions
            description (str): quiz description
        """
        new_quiz = Quiz(
            tutor=tutor, title=title, description=description
        )
        for question in questions:
            try:
                new_question = Question(
                    id=ObjectId(),
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
    def update_quiz(id, tutor, title, questions, description):
        """Updates quiz data
        Args:
            id (str): quiz id
            tutor (user): quiz tutor
            title (str): quiz title
            questions (List(dict)): quiz questions
            description (str): quiz description
        """
        try:
            quiz = QuizService.find_quiz_by_id(id, tutor)
        except Exception as e:
            raise e
        if title:
            quiz.title = title
        if description:
            quiz.description = description

        for question_dict in questions:
            question = None
            try:
                if question_dict.get('id'):
                    question = quiz.questions.get(id=question_dict['id'])
                    print(question.to_json())
                    if question_dict.get('type'):
                        question.type = question_dict['type']
                    if question_dict.get('question'):
                        question.question = question_dict['question']
                    if question_dict.get('correct_answer'):
                        question.correct_answer = question_dict['correct_answer']
                    if question_dict.get('points'):
                        question.points = question_dict['points']
                else:
                    question = Question(
                        type=question_dict['type'],
                        question=question_dict['question'],
                        correct_answer=question_dict['correct_answer'],
                        points=question_dict['points']
                    )
                    quiz.questions.append(question)

                if question_dict.get('options') and question.type == "multiple-choice":
                    question.options = question_dict['options']

            except Exception as err:
                raise err
        quiz.save()

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
