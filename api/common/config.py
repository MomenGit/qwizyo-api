#!/usr/bin/env python3
""""""
import os
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()


class Config:
    """"""
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    # Add other default configuration variables


class DevelopmentConfig(Config):
    """"""
    DEBUG = True
    MONGODB_URI = os.getenv("MONGODB_URI_DEV")
    # Add development-specific configuration variables


class ProductionConfig(Config):
    """"""
    DEBUG = False
    MONGODB_URI = os.getenv("MONGODB_URI")
    # Add production-specific configuration variables


configs = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}

ENV = os.getenv("ENV")
if ENV is None:
    ENV = "dev"

config = configs[ENV]
