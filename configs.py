# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
    CAPTION = "**© By @Dkbotz ❤️**"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))

    PROGRESS = """
"""
    
    ABOUT_TEXT = """
**● Developed By : [Anonymous](https://t.me/dkbotzhelp)
● Updates Channel : [Dkbotz](https://t.me/dkbotz)
● Support : [DkBotz Support](https://t.me/dk_botz)
● Language : [Python 3](https://www.python.org)
● Library : [Pyrogram](https://docs.pyrogram.org)
● Server : [Heroku](https://heroku.com)

©️ Made By @Dkbotz ❤️**
"""

    HELP_TEXT = """**Hello {}, It's too easy to use me..**
 
**● Configure the Settings before using me... 
● Send a photo to set it as your custom thumbnail...
● Send any File or media you want to rename... 
● That's it, and rest is mine work...

📝 Available Commands... 
- /start - Start the Bot
- /help - This Message
- /about - About Meh
- /settings - Configure Settings 
- /showthumb & /deletethumb - For Thumbnail

© By @Dkbotz ❤️**
"""
