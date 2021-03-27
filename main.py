#  Copyright (c) ChernV (@otter18), 2021.

import datetime
import logging
import os
import time

import pytz
import telebot
import tg_logger
from flask import Flask, request

import random

# ------------- uptime var -------------
boot_time = time.time()
boot_date = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow"))

# ------------- flask config -------------
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
app = Flask(__name__)

# ------------- bot config -------------
WEBHOOK_TOKEN = os.environ.get('WEBHOOK_TOKEN')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# ------------- log ---------------
users = [int(os.environ.get("ADMIN_ID"))]

alpha_logger = logging.getLogger()
alpha_logger.setLevel(logging.INFO)
tg_logger.setup(alpha_logger, token=os.environ.get("LOG_BOT_TOKEN"), users=users)
tg_logger.setup(app.logger, token=os.environ.get("LOG_BOT_TOKEN"), users=users)

logger = logging.getLogger("tg-bot-template")


# -------------- status webpage --------------
@app.route('/')
def status():
    password = request.args.get("password")
    if password != ADMIN_PASSWORD:
        logger.info('Status page loaded without password')
        return "<h1>Access denied!<h1>", 403

    return f'<h1>This is telegram bot server, ' \
           f'<a href="https://github.com/otter18/telegram-bot-template">templated</a> by ' \
           f'<a href="https://github.com/otter18">@otter18</a></h1>' \
           f'<p>Server uptime: {datetime.timedelta(seconds=time.time() - boot_time)}</p>' \
           f'<p>Server last boot at {boot_date}'


# ------------- webhook ----------------
@app.route('/' + WEBHOOK_TOKEN, methods=['POST'])
def getMessage():
    temp = request.stream.read().decode("utf-8")
    temp = telebot.types.Update.de_json(temp)
    logger.debug('New message received. raw: %s', temp)
    bot.process_new_updates([temp])
    return "!", 200


@app.route("/set_webhook")
def webhook_on():
    password = request.args.get("password")
    if password != ADMIN_PASSWORD:
        logger.info('Set_webhook page loaded without password')
        return "<h1>Access denied!<h1>", 403

    bot.remove_webhook()
    url = 'https://' + os.environ.get('HOST') + '/' + WEBHOOK_TOKEN
    bot.set_webhook(url=url)
    logger.info(f'Webhook is ON! Url: %s', url)
    return "<h1>WebHook is ON!</h1>", 200


@app.route("/remove_webhook")
def webhook_off():
    password = request.args.get("password")
    if password != ADMIN_PASSWORD:
        logger.info('Remove_webhook page loaded without password')
        return "<h1>Access denied!<h1>", 403

    bot.remove_webhook()
    logger.info('WebHook is OFF!')
    return "<h1>WebHook is OFF!</h1>", 200


# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(message.chat.id,
                     '<b>Hello! This is a telegram bot template written by <a href="https://github.com/otter18">otter18</a></b>',
                     parse_mode='html')


@bot.message_handler(func=lambda message: sum([int(elem in message.text.lower()) for elem in ['привет', 'hello', 'hi', 'privet']]))
def hi(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used hi option:\n\n%s', message.text)
    bot.send_message(message.chat.id, random.choices(['Приветствую', 'Здравствуйте', 'Привет!']))

                     
@bot.message_handler(func=lambda message: sum([int(elem in message.text.lower()) for elem in ['как дела', 'как ты', 'how are you', 'дела', 'how is it going']]))
def howru(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used dela option:\n\n%s', message.text)
    bot.send_message(message.chat.id, random.choices(['Хорошо', 'Отлично', 'Good. And how are u?']))


@bot.message_handler(func=lambda message: sum([int(elem in message.text.lower()) for elem in ['зовут', 'name', 'имя']]))
def name(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used name option:\n\n%s', message.text)
    bot.send_message(message.chat.id, random.choices(['Я telegram-template-bot', 'Я бот шаблон, но ты можешь звать меня в свой проект', 'Это секрет. Используй команду /help, чтобы узнать']))


@bot.message_handler(func=lambda message: True)
def echo(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used echo:\n\n%s', message.text)
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.polling(none_stop=True)
