import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    
    #SQLALCHEMY_DATABASE_URI='mysql+pymysql://temp1:1234@127.0.0.1:3306/data'
    #DO NOT HARDCODE VALUES LIKE THESE
    #USE ENVIRONMENT VARIABLES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
