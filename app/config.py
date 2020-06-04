import pymysql
import os 

class Configuration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Htyg-htyg1$@localhost/test1'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
### Flask security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'