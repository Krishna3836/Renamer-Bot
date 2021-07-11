# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    CAPTION = "Rename Bot by @{}\n\nMade by @AbirHasan2005"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """**Hii {}, I'm a Simple File Renamer Bot with Permanent Thumbnail Support! 💯**
    
**Check Below Buttons for more :**
**🤖 Developer : [Animesh Verma](https://t.me/Animesh941)**
"""
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
    """
    ABOUT_TEXT = """
**● Developer : [Animesh Verma](https://t.me/Animesh941)**
**● Updates Channel : [AV Botz](https://t.me/AVBotz)**
**● Support Group : [Join Now](https://t.me/AVBotz_Support)**
**● Language : [Python3](https://www.python.org)**
**● Library : [Pyrogram](https://docs.pyrogram.org)**
**● Server : [Heroku](https://heroku.com)

© By @AVBotz ❤️**
"""

    HELP_TEXT = """**Hello {}, It's too easy to use me..**
   
**☞︎︎︎ Send a photo to set it as your custom thumbnail.**
**☞︎︎︎ Then Send any File you want to rename.**
**☞︎︎︎ A message will be appeared after your file, reply to it and send the new file name.**
**☞︎︎︎ That's it, and rest is mine work**

**© By @AVBotz ❤️**
"""
