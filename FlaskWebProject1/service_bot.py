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


SERVICE_BOT = telegram.Bot(token=app.config['SERVICE_BOT_TOKEN'])


def get_stat(path):
    with requests.session() as s:
        req = s.get(app.config["BACKGROUND_URL"].format(path))
        if req.status_code == 200:
            return req.content


def date_reader(message):
    date = re.search(r'\d{4}-\d{2}-\d{2}', message)
    if date:
        date = datetime.datetime.strptime(date.group(), '%Y-%m-%d').date() + datetime.timedelta(days=1)
        return get_stat('send_mini_report_text/{}'.format(date.strftime('%Y-%m-%d')))
    else:
        return get_stat(
            'send_mini_report_text/{}'.format(datetime.date.today() + datetime.timedelta(days=1)))


def reply_markup():
    today = datetime.date.today()
    custom_keyboard = [['/*' + ' '*6 + 'статистика за сегодня' + ' '*6 + '*/']]
    for i in range(1, 7):
        next_day = today - datetime.timedelta(days=i)
        custom_keyboard.append(['/*' + ' '*6 + 'статистика за {}'.format(next_day) + ' '*6 + '*/'])
    return telegram.ReplyKeyboardMarkup(custom_keyboard)


service = Blueprint('service', __name__)


@service.route('/hook', methods=['POST'])
def service_webhook_handler():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), SERVICE_BOT)

    chat_id = update.message.chat.id

    # Telegram understands utf-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8')

    if app.config["ATOL_PASSWORD"] in text:
        SERVICE_BOT.sendMessage(chat_id=chat_id,
                        text="Выберете нужное значение",
                        reply_markup=reply_markup())
    elif re.match(r"/\*      статистика за (\d{4}-\d{2}-\d{2}|сегодня)      \*/", text):
        SERVICE_BOT.sendMessage(chat_id=chat_id,
                        text=date_reader(text),
                        reply_markup=reply_markup())
    else:
        SERVICE_BOT.sendMessage(chat_id=chat_id,
                        text="Введите секретный код",
                        reply_markup=telegram.ReplyKeyboardRemove())
    return 'ok'


@service.route('/set_webhook', methods=['GET', 'POST'])
def service_set_webhook():
    s = SERVICE_BOT.setWebhook('{}/service/hook'.format(app.config['HOOK_SITE']))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

