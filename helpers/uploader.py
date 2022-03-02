# (c) @AbirHasan2005

import os
import asyncio
import time
import random
from PIL import Image
from configs import Config
from helpers.clean import delete_one, delete_all
from helpers.display_progress import progress_for_pyrogram, humanbytes
from helpers.database.access_db import db
from helpers.check_gap import CheckTimeGap
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pyrogram import Client

from humanfriendly import format_timespan

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, Thumbnail

async def UploadVideo(bot: Client, cb: CallbackQuery, file_path: str, width, height, duration, video_thumbnail, file_size, default_thumb: Thumbnail = None):
    try:
        sent_ = None
        if (await db.get_upload_as_doc(cb.from_user.id)) is False:
            c_time = time.time()
            sent_ = await bot.send_video(
                chat_id=cb.message.chat.id,
                video=file_path,
                width=width,
                height=height,
                duration=duration,
                thumb=video_thumbnail,
                caption=Config.CAPTION.format((await bot.get_me()).username) + f"\n\n**File Name:** `{merged_vid_path.rsplit('/', 1)[-1]}`\n**Duration:** `{format_timespan(duration)}`\n**File Size:** `{humanbytes(file_size)}`",
                progress=progress_for_pyrogram,
                progress_args=(
                    "Uploading Video ...",
                    cb.message,
                    c_time
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Developer - @AbirHasan2005", url="https://t.me/AbirHasan2005")],
                        [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo"),
                         InlineKeyboardButton("Bots Channel", url="https://t.me/Discovery_Updates")]
                    ]
                )
            )
        else:
            c_time = time.time()
            sent_ = await bot.send_document(
                chat_id=cb.message.chat.id,
                document=file_path,
                caption=Config.CAPTION.format((await bot.get_me()).username) + f"\n\n**File Name:** `{merged_vid_path.rsplit('/', 1)[-1]}`\n**Duration:** `{format_timespan(duration)}`\n**File Size:** `{humanbytes(file_size)}`",
                thumb=video_thumbnail,
                progress=progress_for_pyrogram,
                progress_args=(
                    "Uploading Video ...",
                    cb.message,
                    c_time
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Developer - @AbirHasan2005", url="https://t.me/AbirHasan2005")],
                        [InlineKeyboardButton("Support Group", url="https://t.me/linux_repo"),
                         InlineKeyboardButton("Bots Channel", url="https://t.me/Discovery_Updates")]
                    ]
                )
            )
        await asyncio.sleep(Config.TIME_GAP)
        forward_ = await sent_.forward(chat_id=Config.LOG_CHANNEL)
        await forward_.reply_text(
            text=f"**User:** [{cb.from_user.first_name}](tg://user?id={str(cb.from_user.id)})\n**Username:** `{cb.from_user.username}`\n**UserID:** `{cb.from_user.id}`",
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as err:
        print(f"Failed to Upload Video!\nError: {err}")
        try:
            await cb.message.edit(f"Failed to Upload Video!\n**Error:**\n`{err}`")
        except:
            pass






async def UploadAudio(bot: Client, message: Message, file_path: str, file_size, duration: int, title: str, performer: str):
    try:
        caption_ = await db.get_caption(message.chat.id)
        db_thumbnail = await db.get_thumbnail(message.chat.id)
        file_thumbnail = None
        if db_thumbnail is not None:
            file_thumbnail = await bot.download_media(
                message=db_thumbnail,
                file_name=f"{Config.DOWNLOAD_PATH}/{str(message.chat.id)}/thumbnail/"
            )
            Image.open(file_thumbnail).convert("RGB").save(file_thumbnail)
            img = Image.open(file_thumbnail)
            img.resize((100, 100))
            img.save(file_thumbnail, "JPG")
        c_time = time.time()
        sent_ = await bot.send_audio(
            chat_id=message.chat.id,
            audio=file_path,
            progress=progress_for_pyrogram,
            progress_args=(
                "**📤 Uploading Audio...**",
                message,
                c_time
            ),
            thumb=file_thumbnail,
            duration=(duration if (duration is not None) else 0),
            performer=(performer if (performer is not None) else "Animesh"),
            title=(title if (title is not None) else file_path.rsplit('/', 1)[-1].rsplit(".", 1)[0]),
            caption=((Config.CAPTION.format((await bot.get_me()).username) + f"\n\n**File Name: {file_path.rsplit('/', 1)[-1]}**") if (caption_ is None) else caption_),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("👀 More Amazing Botz 🤖", url="https://t.me/AVBotz/5")]
                ]
            )
        )
        await asyncio.sleep(Config.SLEEP_TIME)
        forward_ = await sent_.forward(chat_id=Config.LOG_CHANNEL)
        await forward_.reply_text(
            text=f"**User: [{message.chat.first_name}](tg://user?id={str(message.chat.id)})\nUsername: {message.chat.username}**",
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as err:
        try:
            await message.edit("**Something Went Wrong... Contact [Here](https://t.me/AVBotz_Support)**")
            await asyncio.sleep(50)
            raise err
        except:
            print(f"**😐 Failed to Upload File!\nError: {err}**")
    await delete_one(file_path)
    if Config.ONE_PROCESS_ONLY:
        await CheckTimeGap(message.chat.id, rm_gap=True)
    await message.delete(True)

