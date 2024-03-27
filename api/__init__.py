from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from mongoengine import connect
from api.common.config import config
from api.common.utils import setup_routes


def create_app(test_config=None):
    """Create and configure the app"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    connect(host=str(app.config["MONGODB_URI"]), alias="default")
    jwt = JWTManager(app)

    api = Api(app)
    api.prefix = '/api'
    setup_routes(api)

    return app
