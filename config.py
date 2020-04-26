import logging
from os import environ as env
import os
from dotenv import load_dotenv
load_dotenv('.env')

class Config:
    '''This class contain environment specific configurations'''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'+env.get('RDS_USER')+':'+env.get('RDS_PASSWORD')+'@'+env.get('RDS_HOSTNAME')+':'+env.get('RDS_PORT')+'/'+env.get('RDS_DBNAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    TESTING = True
    LOG_LEVEL = logging.INFO
    SWAGGER_DISPLAY = bool(int(os.environ.get('SWAGGER_DISPLAY', 0)))
    CELERY_BROKER_URL = 'amqp://localhost/'
    CELERY_RESULT_BACKEND = 'db+postgresql://postgres:postgres@localhost/test'
    ENV = 'development'
ENV = Config