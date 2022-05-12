class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/sqlite/sqlite-tools-win32-x86-3380500/try.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False