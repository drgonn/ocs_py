import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    BROKER_URL = 'redis://redis_ocs:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis_ocs:6379/0'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@postgres_ocs:5432/ocs'

    CELERY_BROKER_URL = 'redis://redis_ocs:6379/0'


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}