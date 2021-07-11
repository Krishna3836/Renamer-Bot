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
    START_TEXT = """**Hii {}, I'm a Simple File Renamer Bot with Permanent Thumbnail Support and many extra features! 💯

👀 Also Configure the Settings for best experience...
👀 Check Below Buttons for more :**

**🤖 Developer : [Animesh Verma](https://t.me/Animesh941)**
"""
    PROGRESS = """
**┈┈••✿ @AVBotz ✿••┈┈

🐌 Speed : {3}/s
📥 Done : {1}
📮 Total size  : {2}
🗑️ Time Left : {4}

✅ Thank You for Using Me..!**"""
    
    ABOUT_TEXT = """
**● Developed By : [This Person](https://t.me/Animesh941)
● Updates Channel : [A𝕍Botz](https://t.me/AVBotz)
● Support : [A𝕍Botz Support](https://t.me/AVBotz_Support)
● Language : [Python 3](https://www.python.org)
● Library : [Pyrogram](https://docs.pyrogram.org)
● Server : [Heroku](https://heroku.com)

©️ Made By @AVBotz ❤️**
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

© By @AVBotz ❤️**
"""
