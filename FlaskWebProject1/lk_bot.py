# -*- coding: utf-8 -*-
import os
import re
import datetime
from app import app
import telegram
from flask import request, Blueprint
import requests
env = os.getenv('SERVER_SOFTWARE')
if env and env.startswith('Google App Engine/'):
    import requests_toolbelt.adapters.appengine
    requests_toolbelt.adapters.appengine.monkeypatch()


LK_BOT = telegram.Bot(token=app.config['LK_BOT_TOKEN'])


lk = Blueprint('lk', __name__)



@lk.route('/hook', methods=['POST'])
def lk_webhook_handler():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), LK_BOT)

    chat_id = update.message.chat.id

    # Telegram understands utf-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8')

    LK_BOT.sendMessage(chat_id=chat_id,
                       text="Привет, твой chat_id: '{}'".format(chat_id))
    return 'ok'


@lk.route('/set_webhook', methods=['GET', 'POST'])
def lk_set_webhook():
    s = LK_BOT.setWebhook('{}/lk/hook'.format(app.config['HOOK_SITE']))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

