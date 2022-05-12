class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite///D:/DB Browser for SQLite/databases/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False