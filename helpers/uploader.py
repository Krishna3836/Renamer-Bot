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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, Thumbnail


async def UploadFile(bot: Client, message: Message, file_path: str, file_size):
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
            img.save(file_thumbnail)
        c_time = time.time()
        sent_ = await bot.send_document(
            chat_id=message.chat.id,
            document=file_path,
            progress=progress_for_pyrogram,
            progress_args=(
                "**📤 Uploading File...**",
                message,
                c_time
            ),
            force_document=True,
            thumb=file_thumbnail,
            caption=((f"**{file_path.rsplit('/', 1)[-1]}**\n\n{Config.CAPTION}") if (caption_ is None) else caption_),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("👀 More Amazing Botz 🤖", url="https://t.me/AVBotz/5")]
                ]
            )
        )
        await asyncio.sleep(Config.SLEEP_TIME)
        forward_ = await sent_.forward(chat_id=Config.LOG_CHANNEL)
        await forward_.reply_text(
            text=f"**User: [{message.chat.first_name}](tg://user?id={str(message.chat.id)})**\n**Username: {message.chat.username}**",
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as err:
        try:
            await message.edit(f"**Failed To Upload, Contact [Here](https://t.me/AVBotz_Support)**")
            await asyncio.sleep(50)
        except:
            print(f"**Failed to Upload File!\nError: {err}**")
    await delete_one(file_path)
    if Config.ONE_PROCESS_ONLY:
        await CheckTimeGap(message.chat.id, rm_gap=True)
    await message.delete(True)


async def UploadVideo(bot: Client, message: Message, file_path: str, file_size, width: int = 100, height: int = 100, duration: int = 0, default_thumb: Thumbnail = None):
    try:
        metadata = extractMetadata(createParser(file_path))
        if (duration == 0) and metadata.has("duration"):
            duration = metadata.get('duration').seconds
        if ((width == 0) or (width == 100)) and metadata.has("width"):
            width = metadata.get("width")
        if ((height == 0) or (height == 100)) and metadata.has("height"):
            height = metadata.get("height")
        db_thumbnail = await db.get_thumbnail(cb.from_user.id)
        if db_thumbnail is not None:
            video_thumbnail = await bot.download_media(message=db_thumbnail, file_name=f"{Config.DOWN_PATH}/{str(cb.from_user.id)}/thumbnail/")
            Image.open(video_thumbnail).convert("RGB").save(video_thumbnail)
            img = Image.open(video_thumbnail)
            img.resize((width, height))
            img.save(video_thumbnail, "JPEG")
        else:
            video_thumbnail = Config.DOWN_PATH + "/" + str(cb.from_user.id) + "/" + str(time.time()) + ".jpg"
            ttl = random.randint(0, int(duration) - 1)
            file_generator_command = [
                "ffmpeg",
                "-ss",
                str(ttl),
                "-i",
                file_path,
                "-vframes",
                "1",
                video_thumbnail
            ]
            process = await asyncio.create_subprocess_exec(
                *file_generator_command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await process.communicate()
            e_response = stderr.decode().strip()
            t_response = stdout.decode().strip()
            if video_thumbnail is None:
                video_thumbnail = None
            else:
                Image.open(video_thumbnail).convert("RGB").save(video_thumbnail)
                img = Image.open(video_thumbnail)
                img.resize((width, height))
                img.save(video_thumbnail, "JPEG")
        await UploadVideo(
            bot=bot,
            cb=cb,
            merged_vid_path=file_path,
            width=width,
            height=height,
            duration=duration,
            video_thumbnail=video_thumbnail,
            file_size=os.path.getsize(merged_vid_path)
        )
        caption = f"© @{(await bot.get_me()).username}"
        if (await db.get_generate_ss(cb.from_user.id)) is True:
            await cb.message.edit("Now Generating Screenshots ...")
            generate_ss_dir = f"{Config.DOWN_PATH}/{str(cb.from_user.id)}"
            list_images = await generate_screen_shots(merged_vid_path, generate_ss_dir, 9, duration)
            if list_images is None:
                await cb.message.edit("Failed to get Screenshots!")
                await asyncio.sleep(Config.TIME_GAP)
            else:
                await cb.message.edit("Generated Screenshots Successfully!\nNow Uploading ...")
                photo_album = list()
                if list_images is not None:
                    i = 0
                    for image in list_images:
                        if os.path.exists(str(image)):
                            if i == 0:
                                photo_album.append(InputMediaPhoto(media=str(image), caption=caption))
                            else:
                                photo_album.append(InputMediaPhoto(media=str(image)))
                            i += 1
                await bot.send_media_group(
                    chat_id=cb.from_user.id,
                    media=photo_album
                )
        if ((await db.get_generate_sample_video(cb.from_user.id)) is True) and (duration >= 15):
            await cb.message.edit("Now Generating Sample Video ...")
            sample_vid_dir = f"{Config.DOWN_PATH}/{cb.from_user.id}/"
            ttl = int(duration*10 / 100)
            sample_video = await cult_small_video(
                video_file=merged_vid_path,
                output_directory=sample_vid_dir,
                start_time=ttl,
                end_time=(ttl + 10),
                format_=FormtDB.get(cb.from_user.id)
            )
            if sample_video is None:
                await cb.message.edit("Failed to Generate Sample Video!")
                await asyncio.sleep(Config.TIME_GAP)
            else:
                await cb.message.edit("Successfully Generated Sample Video!\nNow Uploading ...")
                sam_vid_duration = 5
                sam_vid_width = 100
                sam_vid_height = 100
                try:
                    metadata = extractMetadata(createParser(sample_video))
                    if metadata.has("duration"):
                        sam_vid_duration = metadata.get('duration').seconds
                    if metadata.has("width"):
                        sam_vid_width = metadata.get("width")
                    if metadata.has("height"):
                        sam_vid_height = metadata.get("height")
                except:
                    await cb.message.edit("Sample Video File Corrupted!")
                    await asyncio.sleep(Config.TIME_GAP)
                try:
                    c_time = time.time()
                    await bot.send_video(
                        chat_id=cb.message.chat.id,
                        video=sample_video,
                        thumb=video_thumbnail,
                        width=sam_vid_width,
                        height=sam_vid_height,
                        duration=sam_vid_duration,
                        caption=caption,
                        progress=progress_for_pyrogram,
                        progress_args=(
                            "Uploading Sample Video ...",
                            cb.message,
                            c_time,
                        )
                    )
                except Exception as sam_vid_err:
                    print(f"Got Error While Trying to Upload Sample File:\n{sam_vid_err}")
                    try:
                        await cb.message.edit("Failed to Upload Sample Video!")
                        await asyncio.sleep(Config.TIME_GAP)
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
            img.save(file_thumbnail)
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
            caption=((f"**{file_path.rsplit('/', 1)[-1]}**\n\n{Config.CAPTION}") if (caption_ is None) else caption_),
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
            await message.edit(f"**Failed To Upload, Contact [Here](https://t.me/AVBotz_Support)**")
            await asyncio.sleep(50)
            raise err
        except:
            print(f"**😐 Failed to Upload File!\nError: {err}**")
    await delete_one(file_path)
    if Config.ONE_PROCESS_ONLY:
        await CheckTimeGap(message.chat.id, rm_gap=True)
    await message.delete(True)
