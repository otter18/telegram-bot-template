# ![logo](https://raw.githubusercontent.com/otter18/telegram-bot-template/main/img/tg-logo.png) Telegram bot [![GitHub Repo stars](https://img.shields.io/github/stars/otter18/telegram-bot-template?style=social)](https://github.com/otter18/telegram-bot-template/stargazers)

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/otter18/telegram-bot-template?label=release)
[![GitHub](https://img.shields.io/github/license/otter18/telegram-bot-template)](https://github.com/otter18/telegram-bot-template/blob/main/LICENSE)

Setup guide is available in [this article](https://habr.com/ru/post/549178/) (RU)

- This bot is meant to be hosted on [Heroku](https://www.heroku.com/home)
- Telegram webhook is connected with flask

## Environment variables

### Main bot
- `BOT_TOKEN` - bot token for main bot
- `WEBHOOK_TOKEN` - large random string to protect webhook
- `ADMIN_PASSWORD` - large random string to access server

### Server settings
- `HOST` - host to set as webhook, e.g *example.herokuapp.com*
- `IS_PRODUCTION` - flag to run flask server or to use bot polling instead

### Tg-logger, [[repo]](https://github.com/otter18/tg_logger)
- `LOG_BOT_TOKEN` - bot token for logging, leave empty to disable
- `ADMIN_ID` - user_id to send logs to


## Webserver pages
- `/?password={ADMIN_PASSWORD}` - status page
- `/set_webhook?password={ADMIN_PASSWORD}` - setup webhook
- `/remove_webhook?password={ADMIN_PASSWORD}` - remove webhook

## Demo

### Bot
![main bot scr](https://raw.githubusercontent.com/otter18/telegram-bot-template/main/img/main.png)
### Tg-logger
![logger scr](https://raw.githubusercontent.com/otter18/telegram-bot-template/main/img/logger.png)
