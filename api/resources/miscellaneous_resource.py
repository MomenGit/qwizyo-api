#!/usr/bin/env python3
"""Defines Resources for Miscellaneous Routes"""
from flask_restful import Resource


class Status(Resource):
    """Status Resource Routes handler"""

    def get(self):
        """"""
        return "pong", 200


class Docs(Resource):
    """Documentation Resource Routes handler"""

    def get(self):
        """"""
        return {}, 200
