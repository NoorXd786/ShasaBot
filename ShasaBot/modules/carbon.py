from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from ShasaBot import SHASA_PHOTO, SUPPORT_CHAT, pbot
from ShasaBot.utils.carbon import make_carbon
from ShasaBot.utils.errors import capture_err


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


@pbot.on_message(filters.command("alive"))
async def alive(_, message):
    await message.reply_photo(
        photo=SHASA_PHOTO,
        caption=f"""⚡ **Hᴇʏ I Aᴍ Sʜᴀsᴀ Rᴏʙᴏᴛ** 

**✨ Cʀᴇᴀᴛᴇᴅ ʙʏ : [Mᴅ Nᴏᴏʀ](t.me/Md_Noor786)**
**🐍 Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{y()}`
**📃 ᴘᴛʙ Vᴇʀsɪᴏɴ :** `{o}`
**💫 Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{s}`
**💥 Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{z}`

**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/LionXupdates"),
                ]
            ]
        ),
    )
