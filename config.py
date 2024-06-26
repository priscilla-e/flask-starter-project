import os
import logging
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'set this key in .env file'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') \
                              or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
