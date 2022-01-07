from pyrogram import filters
from pyrogram.errors import RPCError

from ShasaBot import pbot
from ShasaBot.pyrogramee.pluginshelper import admins_only, get_text


@pbot.on_message(
    filters.command("captedit") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def loltime(client, message):
    lol = await message.reply("Processing please wait")
    cap = get_text(message)
    if not message.reply_to_message:
        await lol.edit("reply to any message to edit caption")
    reply = message.reply_to_message
    try:
        await reply.copy(message.chat.id, caption=cap)
        await lol.delete()
    except RPCError as i:
        await lol.edit(i)
        return
