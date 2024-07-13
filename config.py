import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/db_compro'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
