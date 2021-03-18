# Telegram bot
- This bot is meant to be hosted on [Heroku](https://www.heroku.com/home)
- Telegram webhook is connected with flask

## Environment variables

### Main bot
- `BOT_TOKEN` - bot token for main bot
- `WEBHOOK_TOKEN` - large random string to protect webhook
- `ADMIN_PASSWORD` - large random string to access server

### Server settings
- `HOST` - host to set as webhook, e.g *example.herokuapp.com*
- `IS_PRODUCTION` - flag to run flask server or use bot polling instead

### Tg-logger, [[repo]](https://github.com/otter18/tg_logger)
- `LOG_BOT_TOKEN` - bot token for logging
- `ADMIN_ID` - user_id to send logs to


## Webserver pages
- `/?password={ADMIN_PASSWORD}` - status page
- `/set_webhook?password={ADMIN_PASSWORD}` - setup webhook
- `/remove_webhook?password={ADMIN_PASSWORD}` - remove webhook