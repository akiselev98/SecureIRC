import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
     #                         'sqlite:///' + os.path.join(basedir, 'app.db')


    #***NOTE: The change the user and password below in order to connect to the SQL server


    SQLALCHEMY_DATABASE_URI='mysql+pymysql://temp1:1234@127.0.0.1:3306/data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
