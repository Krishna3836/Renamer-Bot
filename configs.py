# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
    CAPTION = "**© By @Tellybots 💕**"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))

    START_TEXT = """Hey {} 🙋

I am a TG Renamer bot with permanent thumbnail support.

Press /settings to change my settings ⚙.

📛 For More Details check Help

Maintained By:  [Tellybots](t.me/Tellybots)

"""
    PROGRESS = """
🔰 Sᴘᴇᴇᴅ : {3}/s\n\n
🌀 Dᴏɴᴇ : {1}\n\n
🎥 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""
    
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [Renamer ʙᴏᴛ](http://t.me/MediaRenamerBot)

**Cʜᴀɴɴᴇʟ** : [Tᴇʟʟʏʙᴏᴛs](https://t.me/TellyBots)

**Vᴇʀꜱɪᴏɴ** : [2.0 ʙᴇᴛᴀ](https://t.me/TellyUploaderRobot)

**Sᴏᴜʀᴄᴇ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/tellybots_digital)

**Sᴇʀᴠᴇʀ** : [ʜᴇʀᴏᴋᴜ](https://heroku.com/)

**Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 3.10.2](https://www.python.org/)

**Fʀᴀᴍᴇᴡᴏʀᴋ :** [ᴘʏʀᴏɢᴀᴍ 1.3.6](https://docs.pyrogram.org/)

**Dᴇᴠᴇʟᴏᴘᴇʀ :** [Tᴇʟʟʏʙᴏᴛs](https://t.me/tellybots)

**Pᴏᴡᴇʀᴇᴅ ʙʏ :** [NᴀʏsᴀBᴏᴛs](https://t.me/NaysaBots)

"""

    HELP_TEXT = """Yᴏᴜ ɴᴇᴇᴅ Hᴇʟᴘ ?? 😅
   
✵ Fɪʀsᴛ ɢᴏ ᴛᴏ ᴛʜᴇ /sᴇᴛᴛɪɴɢs ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙᴏᴛ ʙᴇʜᴀᴠɪᴏʀ ᴀs ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

✵ Sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴀᴠᴇ ɪᴛ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ. (𝚘𝚙𝚝𝚒𝚘𝚗𝚊𝚕)

✵ Nᴏᴡ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ.

✵ Aғᴛᴇʀ ᴛʜᴀᴛ ʙᴏᴛ ᴡɪʟʟ ᴀsᴋ ʏᴏᴜ ғᴏʀ ᴛʜᴇ Nᴇᴡ Nᴀᴍᴇ ᴛʜᴇɴ sᴇɴᴅ ᴛʜᴇ Nᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ᴏʀ ᴡɪᴛʜᴏᴜᴛ Exᴛᴇɴᴛɪᴏɴ.

✵ Tʜᴇɴ ʙᴇ ʀᴇʟᴀxᴇᴅ ʏᴏᴜʀ ғɪʟᴇ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ sᴏᴏɴ..


⚠️ Nᴏᴛᴇ: Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴀɴɢᴇ ʙᴏᴛ ᴄᴀᴘᴛɪᴏɴ Gᴏ ᴛᴏ /settings >> Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
"""
