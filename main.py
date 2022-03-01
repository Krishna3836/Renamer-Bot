# (c) @AbirHasan2005

import os
import time
import psutil
import shutil
import string
import asyncio
from pyromod import listen
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply

from configs import Config
from helpers.settings import OpenSettings
from helpers.database.access_db import db
from helpers.forcesub import ForceSub
from helpers.check_gap import CheckTimeGap
from helpers.setup_prefix import SetupPrefix
from helpers.broadcast import broadcast_handler
from helpers.uploader import UploadFile, UploadVideo, UploadAudio
from helpers.database.add_user import AddUserToDatabase
from helpers.display_progress import progress_for_pyrogram, humanbytes

RenameBot = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🚴 Oᴡɴᴇʀ', url='https://telegram.me/Tellybots'),
        InlineKeyboardButton('🌀 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('💡 ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('⚙️ Sᴇᴛᴛɪɴɢs', callback_data='openSettings')
        ],[
        InlineKeyboardButton('🗑️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔰 Hᴏᴍᴇ", callback_data="home"),
                 InlineKeyboardButton("🌀 ᴀʙᴏᴜᴛ", callback_data="about"),
                 InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
            ]
        )

ABOUT_BUTTONS = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📝 Fᴇᴇᴅʙᴀᴄᴋ ᴅᴇᴠ", url="https://t.me/Tellybots_support")],
                [InlineKeyboardButton("🔰 Hᴏᴍᴇ", callback_data="home"),
                 InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ", callback_data="close")]
            ]
        )


@RenameBot.on_message(filters.private & filters.command("start"))
async def start_handler(bot: Client, event: Message, cb=False):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    if not cb:
        send_msg = await event.reply_text("**👀 Pʀᴏᴄᴇssɪɴɢ......**", quote=True)    
    await send_msg.edit(
      text=f"{Config.START_TEXT}".format(event.from_user.mention), 
      reply_markup=START_BUTTONS, 
      disable_web_page_preview=True
       )
    if cb:
        return await event.message.edit(
                 text=f"{Config.START_TEXT}".format(event.from_user.mention),
                 reply_markup=START_BUTTONS,
                 disable_web_page_preview=True
                     )
            
@RenameBot.on_message(filters.private & filters.command("help"))
async def start_handler(bot: Client, event: Message, cb=False):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    if not cb:
        send_msg = await event.reply_text("**👀 Pʀᴏᴄᴇssɪɴɢ......**", quote=True)    
    await send_msg.edit(
      text=f"{Config.HELP_TEXT}".format(event.from_user.mention), 
      reply_markup=HELP_BUTTONS, 
      disable_web_page_preview=True
       )
    if cb:
        return await event.message.edit(
                 text=f"{Config.HELP_TEXT}".format(event.from_user.mention),
                 reply_markup=HELP_BUTTONS,
                 disable_web_page_preview=True
                     )
            
@RenameBot.on_message(filters.private & filters.command("about"))
async def start_handler(bot: Client, event: Message, cb=False):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    if not cb:
        send_msg = await event.reply_text("**👀 Pʀᴏᴄᴇssɪɴɢ......**", quote=True)    
    await send_msg.edit(
      text=f"{Config.ABOUT_TEXT}", 
      reply_markup=ABOUT_BUTTONS, 
      disable_web_page_preview=True
       )
    if cb:
        return await event.message.edit(
                 text=f"{Config.ABOUT_TEXT}",
                 reply_markup=ABOUT_BUTTONS,
                 disable_web_page_preview=True
                     )


