# -*- coding: utf-8 -*-
# Конфигурация приложения
import os
import sys

# приложение
DEBUG = True
env = os.getenv('SERVER_SOFTWARE')

if env and env.startswith('Google App Engine/'):
    version_name = os.environ['CURRENT_VERSION_ID']

SERVICE_BOT_TOKEN = ""
LK_BOT_TOKEN = ""
HOOK_SITE = ''
BACKGROUND_URL = '/{}'
LKAPI_URL = '/{}'
ATOL_PASSWORD = ""


env = os.getenv('SERVER_SOFTWARE')

if env and env.startswith('Google App Engine/'):
    version_name = os.environ['CURRENT_VERSION_ID']

if env and env.startswith('Google App Engine/'):
    # Connecting from App Engine
    db_name = 'telegram'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@/{}?unix_socket=/cloudsql/atol-accountapi:us-central1:cloudbd?charset=utf8'.format(db_name)
else:
    # Connecting from an external network.
    # Make sure your network is whitelisted
    if 'win' in sys.platform:
        SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/telegram?charset=utf8'
    else:
        SQLALCHEMY_DATABASE_URI = 'mysql://root@104.196.55.149:3306/telegram?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 50


SECRET_KEY = "A_gU10_!SecretKey\n"
