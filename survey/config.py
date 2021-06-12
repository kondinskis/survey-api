import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_ECHO = True
    JWT_ERROR_MESSAGE_KEY = "message"
    JWT_SECRET_KEY = os.getenv("SECRET_KEY")
    ERROR_404_HELP = False