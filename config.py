# -*- coding: utf-8 -*-
# Конфигурация приложения
import os
import sys

# приложение
DEBUG = True
env = os.getenv('SERVER_SOFTWARE')

if env and env.startswith('Google App Engine/'):
    version_name = os.environ['CURRENT_VERSION_ID']

SERVICE_BOT_TOKEN = "297866660:AAHPAG4t4YfNYReGW11RqNY1eSVNUR0OrcI"
LK_BOT_TOKEN = "301869424:AAE250BilXf2kB9kpL-GwZ6GytDoyLfN9RE"
HOOK_SITE = 'https://telegrambot-dot-atol-accountapi.appspot.com'
BACKGROUND_URL = 'https://background-dot-atol-accountapi.appspot.com/{}'
LKAPI_URL = 'https://develop-dot-atol-accountapi.appspot.com/{}'
ATOL_PASSWORD = "lkpas@2017"


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
