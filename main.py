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
        send_msg = await event.reply_text("**👀 Processing......**", quote=True)    
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
        send_msg = await event.reply_text("**👀 Processing......**", quote=True)    
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
        send_msg = await event.reply_text("**👀 Processing......**", quote=True)    
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


            #try:
                #os.remove(download_location)
              #  os.remove(thumb_image_path)
            #except:
                #pass

@RenameBot.on_message(filters.private & (filters.video | filters.document | filters.audio))
async def rename_handler(bot: Client, event: Message):
        download_location = f"{Config.DOWNLOAD_PATH}/{str(event.from_user.id)}/{str(time.time())}/"
        if os.path.exists(download_location):
            os.makedirs(download_location)
        await reply_("**👀 Processing...**")
        c_time = time.time()
        try:
            await bot.download_media(
                message=event,
                file_name=new_file_name,
                progress=progress_for_pyrogram,
                progress_args=(
                    "Downloading File ...",
                    reply_,
                    c_time
                )
            )
            await asyncio.sleep(Config.SLEEP_TIME)
            await reply_.edit("Uploading File ...")
            upload_as_doc = await db.get_upload_as_doc(event.from_user.id)
            if upload_as_doc is True:
                await UploadFile(
                    bot,
                    reply_,
                    file_path=new_file_name,
                    file_size=media.file_size
                )
            else:
                if event.audio:
                    duration_ = event.audio.duration if event.audio.duration else 0
                    performer_ = event.audio.performer if event.audio.performer else None
                    title_ = event.audio.title if event.audio.title else None
                    await UploadAudio(
                        bot,
                        reply_,
                        file_path=new_file_name,
                        file_size=media.file_size,
                        duration=duration_,
                        performer=performer_,
                        title=title_
                    )
                elif event.video or (event.document and event.document.mime_type.startswith("video/")):
                    thumb_ = event.video.thumbs[0] if ((event.document is None) and (event.video.thumbs is not None)) else None
                    duration_ = event.video.duration if ((event.document is None) and (event.video.thumbs is not None)) else 0
                    width_ = event.video.width if ((event.document is None) and (event.video.thumbs is not None)) else 0
                    height_ = event.video.height if ((event.document is None) and (event.video.thumbs is not None)) else 0
                    await UploadVideo(
                        bot,
                        reply_,
                        file_path=new_file_name,
                        file_size=media.file_size,
                        default_thumb=thumb_,
                        duration=duration_,
                        width=width_,
                        height=height_
                    )
                else:
                    await UploadFile(
                        bot,
                        reply_,
                        file_path=new_file_name,
                        file_size=media.file_size
                    )


@RenameBot.on_message(filters.private & filters.photo & ~filters.edited)
async def photo_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    editable = await event.reply_text("Please Wait ...")
    await db.set_thumbnail(event.from_user.id, thumbnail=event.photo.file_id)
    await editable.edit("Permanent Custom Thumbnail Saved Successfully!")


@RenameBot.on_message(filters.private & filters.command(["delete_thumbnail", "delete_thumb", "del_thumb", "delthumb"]) & ~filters.edited)
async def delete_thumb_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await db.set_thumbnail(event.from_user.id, thumbnail=None)
    await event.reply_text(
        "Custom Thumbnail Deleted Successfully!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Go To Settings", callback_data="openSettings")],
            [InlineKeyboardButton("Close", callback_data="closeMeh")]
        ])
    )


@RenameBot.on_message(filters.private & filters.command(["show_thumbnail", "show_thumb", "showthumbnail", "showthumb"]) & ~filters.edited)
async def show_thumb_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    _thumbnail = await db.get_thumbnail(event.from_user.id)
    if _thumbnail is not None:
        try:
            await bot.send_photo(
                chat_id=event.chat.id,
                photo=_thumbnail,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Delete Thumbnail", callback_data="deleteThumbnail")]]
                ),
                reply_to_message_id=event.message_id
            )
        except Exception as err:
            try:
                await bot.send_message(
                    chat_id=event.chat.id,
                    text=f"Unable to send Thumbnail!\n\n**Error:** `{err}`",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❎ Close ❎", callback_data="closeMeh")]]),
                    reply_to_message_id=event.message_id
                )
            except:
                pass
    else:
        await event.reply_text("No Thumbnail Found in Database!\nSend a Thumbnail to Save.", quote=True)


@RenameBot.on_message(filters.private & filters.command(["delete_caption", "del_caption", "remove_caption", "rm_caption"]) & ~filters.edited)
async def delete_caption(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    await db.set_caption(event.from_user.id, caption=None)
    await event.reply_text("Custom Caption Removed Successfully!")


@RenameBot.on_message(filters.private & filters.command("broadcast") & filters.user(Config.BOT_OWNER) & filters.reply)
async def _broadcast(_, event: Message):
    await broadcast_handler(event)


@RenameBot.on_message(filters.private & filters.command("status") & filters.user(Config.BOT_OWNER))
async def show_status_count(_, event: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await event.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )


@RenameBot.on_message(filters.private & filters.command("settings"))
async def settings_handler(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    FSub = await ForceSub(bot, event)
    if FSub == 400:
        return
    editable = await event.reply_text(
        text="Please Wait ..."
    )
    await OpenSettings(editable, user_id=event.from_user.id)





RenameBot.run()
