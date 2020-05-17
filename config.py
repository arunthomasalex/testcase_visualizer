import os

class Config(object):
    DEBUG = False
    SECRET_KEY = 'dev'
    DATABASE=os.path.join(os.path.abspath(__name__), '..', 'instance', 'flaskr.sqlite')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True