# (c) @AbirHasan2005

import asyncio
from helpers.database.access_db import db
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(event: Message, user_id: int):
    try:
        await event.edit(
            text="**__⚙ Configure my Behavior from here, to experience the best service 😉\n\n© @Dkbotz ❤️__**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"📤 Upload as Document {'✅' if ((await db.get_upload_as_doc(user_id)) is True) else '❌'}",
                                          callback_data="triggerUploadMode")],
                    [InlineKeyboardButton("📸 Custom Thumbnail ", callback_data="triggerThumbnail")],
                    [InlineKeyboardButton("📮 Custom Caption ", callback_data="triggerCaption")],
                    [InlineKeyboardButton("⛔ Close Settings ⛔", callback_data="closeMeh")]
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await OpenSettings(event, user_id)
    except MessageNotModified:
        pass
