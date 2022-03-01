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

    START_TEXT = """<b>Hey</b> <b>{}</b> 🙋

<code>I am a TG Renamer bot with permanent thumbnail support.</code>

<b>Press /settings to change my settings ⚙.</b>

📛 For More Details check <b>Help</b>

<b>Maintained By:</b> <b> [Tellybots](t.me/Tellybots)</b>
"""
    PROGRESS = """
🔰 Speed : {3}/s\n\n
🌀 Done : {1}\n\n
🎥 Total size  : {2}\n\n
⏳ Time Left : {4}\n\n
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

    HELP_TEXT = """You need Help ?? 😅
   
✵ First go to the /settings and change the bot behavior as your choice.

✵ Send me the custom thumbnail to save it permanently. (𝚘𝚙𝚝𝚒𝚘𝚗𝚊𝚕)

✵ Now send me the file or video which you want to rename.

✵ After that bot will ask you for the New Name then send the New file name with or without Extention.

✵ Then be relaxed your file will be uploaded soon..


⚠️ Note: If you want to change bot caption use command /set_caption
"""
