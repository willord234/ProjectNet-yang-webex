from webex_bot.webex_bot import WebexBot

import os

webex_token = os.environ["WEBEX_TOKEN"]

bot = WebexBot(webex_token, approved_users=["willordplotena@gmail.com"])

bot.run()