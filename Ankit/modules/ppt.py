import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Ankit.events import register
from Ankit import telethn as tbot


PHOTO = [ "https://telegra.ph/file/117e9fdda7a7621d5e106.jpg",
          "https://telegra.ph/file/e441fed95804b41b1326a.jpg",
          "https://telegra.ph/file/21c6c1974c85f386b3523.jpg",
          "https://telegra.ph/file/32f6f217e1d71b5fbdcb4.jpg",
          "https://telegra.ph/file/8a08b66b51c8af4155cc5.jpg",
          "https://telegra.ph/file/aac4a2d3a7dc8dc7b8372.jpg",
          "https://telegra.ph/file/8cc851e5f40ae728bfaa9.jpg",
          "https://telegra.ph/file/10e0f8893cec365756b3c.jpg"
        ]

@register(pattern=("/ppt"))
async def awake(event):
  TEXT = f"HOW TO OPEN THIS BOT"
  TEXT = f"â¢ððð ððð ðððð ðð ðð ððððððððð ððð ðððððððð @NVS_X_BOt  ðð ððð ðððððððð."
  TEXT = f"â¢YOU CAN ALSO OPEN IT BY CLICKING OR SEARCHING THE LINK  https://t.me/NVS_X_BOT"
  TEXT = f"HOW CAN YOU BE SAFE IN TODAY'S DIGITAL WORLD? IS THERE ANY SOLUTION FOR IT? YES, WE HAVE A SOLUTION FOR IT."
  TEXT = f"A POWERFUL GROUP MANAGEMENT BOT BUILD TO HELP YOU MANAGE YOUR TELEGRAM GROUP EASILY AND TO PROTECT YOUR GROUP FROM DIGITAL ATTACKS."
  TEXT = f"ê® HAVE THE NORMAL GROUP MANAGING FUNCTION LIKE WARNING SYSTEM, LOGO MAKING AND A LOT. BUT I MAINLY HAVE THE ADVANCED AND HANDY ANTISPAM SYSTEM AND THE BANNING SYSTEM WHICH SAFEGUARDS AND HELP YOUR GROUP FROM BEING SCAMMED OR SPAMMED."
  TEXT = f"FUNCTIONS OF OUR BOT"
  TEXT = f"â²  I CAN RESTRICTS USERS."
  TEXT = f"â²  I CAN GREET USERS WITH CUSTOMIZABLE WELCOME MESSAGES AND EVEN SET A GROUP'S RULES."
  TEXT = f"â² I HAVE NOTE KEEPING SYSTEM, BLACKLIST, AND EVEN PREDETERMINED REPLIES ON CERTAIN KEYBOARDS."
  TEXT = f"â² I CHECK FOR ADMINS PERMISSION BEFORE EXECUTING ANY COMMAND AND MORE STUFFS."
  TEXT = f"THIS PROJECT CAN HELP THE SOCIETY FROM BEING ROBBED, CHEATED AND THEY CAN GET A SECURE MODE OF COMMUNICATION."
  TEXT = f"ð£ðððð  ð¨ðð¤"

 
  await tbot.send_file(event.chat_id, ran, caption=TEXT)

## Alive mod By @XNKIT
