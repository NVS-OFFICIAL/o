import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Ankit.events import register
from Ankit import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/17305d0a45a7ed3ef9d9d.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),ɪ ᴀᴍ ᴘʀᴏᴊᴇᴄᴛ-x **\n━━━━━━━━━━━━━━━━━━━\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ᴛᴇᴀᴍ ᴘʀᴏᴊᴇᴄᴛ-x](https://github.com/nvs-official)** \n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("🔹ʜᴇʟᴘ🔹", "https://t.me/NVS_X_BOT?start=help"), Button.url("⭐ᴅᴇᴠᴇʟᴏᴘᴇʀ⭐", "https://github.com/nvs-official")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod By @XNKIT
