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
    "https://telegra.ph/file/273cb09e8e0425cca997e.jpg",
]

@register(pattern=("/ppt"))
async def awake(event):
  TEXT = f"HOW TO OPEN THIS BOT​"
  TEXT = f"•𝐘𝐎𝐔 𝐂𝐀𝐍 𝐎𝐏𝐄𝐍 𝐈𝐓 𝐁𝐘 𝐒𝐄𝐀𝐑𝐂𝐇𝐈𝐍𝐆 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 @NVS_X_BOT​   𝐈𝐍 𝐓𝐇𝐄 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌."
  TEXT = f"•YOU CAN ALSO OPEN IT BY CLICKING OR SEARCHING THE LINK  https://t.me/NVS_X_BOT​"
  TEXT = f"HOW CAN YOU BE SAFE IN TODAY'S DIGITAL WORLD? IS THERE ANY SOLUTION FOR IT? YES, WE HAVE A SOLUTION FOR IT."
  TEXT = f"A POWERFUL GROUP MANAGEMENT BOT BUILD TO HELP YOU MANAGE YOUR TELEGRAM GROUP EASILY AND TO PROTECT YOUR GROUP FROM DIGITAL ATTACKS.​​"
  TEXT = f"Ɪ HAVE THE NORMAL GROUP MANAGING FUNCTION LIKE WARNING SYSTEM, LOGO MAKING AND A LOT. BUT I MAINLY HAVE THE ADVANCED AND HANDY ANTISPAM SYSTEM AND THE BANNING SYSTEM WHICH SAFEGUARDS AND HELP YOUR GROUP FROM BEING SCAMMED OR SPAMMED."
  TEXT = f"FUNCTIONS OF OUR BOT​"
  TEXT = f"➲  I CAN RESTRICTS USERS. ​"
  TEXT = f"➲  I CAN GREET USERS WITH CUSTOMIZABLE WELCOME MESSAGES AND EVEN SET A GROUP'S RULES.​"
  TEXT = f"➲ I HAVE NOTE KEEPING SYSTEM, BLACKLIST, AND EVEN PREDETERMINED REPLIES ON CERTAIN KEYBOARDS.​"
  TEXT = f"➲ I CHECK FOR ADMINS PERMISSION BEFORE EXECUTING ANY COMMAND AND MORE STUFFS.​"
  TEXT = f"THIS PROJECT CAN HELP THE SOCIETY FROM BEING ROBBED, CHEATED AND THEY CAN GET A SECURE MODE OF COMMUNICATION."
  TEXT = f"𝓣𝓗𝓐𝓝𝓚  𝓨𝓞𝓤​"

  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod By @XNKIT
