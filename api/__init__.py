from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from api.resources import auth_resource, user_resource
from mongoengine import connect

api = Api()


def init_db(app: Flask):
    """"""
    app.config["MONGODB_SETTINGS"] = [
        {
            "db": "qwizyo",
            "host": "localhost",
            "port": 27017,
            "alias": "default",
        }]
    connect(db="qwizyo",
            host="localhost",
            port=27017,
            alias="default",)


def init_api(app: Flask):
    """"""
    api.prefix = '/api'

    api.add_resource(user_resource.User, '/users/<string:id>')
    api.add_resource(auth_resource.RegisterAuth, '/auth/register')
    api.add_resource(auth_resource.LoginAuth, '/auth/login')
    """ api.add_resource('/quizzes')
    api.add_resource('/quizzes/<str:id>')
    api.add_resource('/groups')
    api.add_resource('/groups/<str:id>')
    api.add_resource('/assignments')
    api.add_resource('/assignments/<str:id>') """
    api.init_app(app)


def create_app(test_config=None):
    """Create and configure the app"""

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    init_api(app)
    init_db(app)

    return app
