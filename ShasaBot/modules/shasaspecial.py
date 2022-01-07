import os
import random
import re

from telethon import *
from telethon.tl.types import *

from ShasaBot import *
from ShasaBot import ubot
from ShasaBot.events import register

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


@register(pattern="^/animate (.*)")
async def stickerizer(event):

    newtext = event.pattern_match.group(1)
    animus = [20, 32, 33, 40, 41, 42, 58]
    sticcers = await ubot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(newtext))}"
    )
    null = await sticcers[0].download_media(TEMP_DOWNLOAD_DIRECTORY)
    bara = str(null)
    await event.client.send_file(event.chat_id, bara, reply_to=event.id)
    os.remove(bara)


__help__ = """
 |• /logo text :  Create Your logo with your name
 |• /slogo text : Create Your Logo With Your Name
 |• /wlogo text :  Create Your logo with your name
 |• /rlogo text :  Create Your logo with Random Color
 |• /nlogo text ; Create Your logo with your name
 |• /animate text : Randomly Generate Stickers with Given Text
 |• /carbon text : replies to message to make carbon
 |• /mmf upper text ; lower text : reply to sticker or image
 """
__mod_name__ = "◎Cʀᴀғᴛ"
