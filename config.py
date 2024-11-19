from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Config:
  SECRET_KEY =  '3311546193mysqlchanchitofeliz'
  DEBUG      = True

class DevelopmentConfig(Config):
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'mysql'
    MYSQL_DB = 'E-motors'
    # python anywhere
    '''MYSQL_HOST = 'emotors.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'emotors'
    MYSQL_PASSWORD = '3311546193Aa@'
    MYSQL_DB = 'e-motors'''

config = {
    'development' : DevelopmentConfig
  }