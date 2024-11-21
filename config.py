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

class MailConfig(Config):
        MAIL_SERVER    = 'smtp.gmail.com'
        MAIL_PORT      = 587
        MAIL_USE_TLS   = True
        MAIL_USE_SSL   = False
        MAIL_USERNAME  = 'gerardo.godinez1811@alumnos.udg.mx'
        MAIL_PASSWORD  = 'lika mgpt kbgu wqgk'
        MAIL_ASCII_ATTACHMENTS = True
        MAIL_DEFAULT_SENDER = 'gerardo.godinez1811@alumnos.udg.mx'

# Corregir el diccionario 'config' añadiendo la coma
config = {
    'development': DevelopmentConfig,
    'mail': MailConfig
}
