import logging
import os

import telebot
import tg_logger
from flask import Flask

# ------------- bot -------------
bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

# ------------- flask app -------------
app = Flask(__name__)

# ------------- logging -------------
logger = logging.getLogger("tg-bot-template")

alpha_logger = logging.getLogger()
alpha_logger.setLevel(logging.INFO)

app.logger.setLevel(logging.ERROR)
telebot.logger.setLevel(logging.ERROR)

users = [int(os.environ.get("ADMIN_ID"))]

if os.environ.get("LOG_BOT_TOKEN", '') != '':
    tg_logger.setup(alpha_logger, token=os.environ.get("LOG_BOT_TOKEN"), users=users)
    tg_logger.setup(app.logger, token=os.environ.get("LOG_BOT_TOKEN"), users=users)
    tg_logger.setup(telebot.logger, token=os.environ.get("LOG_BOT_TOKEN"), users=users)

# ------------- webhook -------------
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
WEBHOOK_TOKEN = os.environ.get('WEBHOOK_TOKEN')
