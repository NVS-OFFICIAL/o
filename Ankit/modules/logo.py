import os
import io
import requests
import shutil 
import random
import re
import glob
import time

from io import BytesIO
from requests import get
from telethon.tl.types import InputMessagesFilterPhotos

from Ankit import OWNER_ID
from Ankit.events import register
from Ankit import telethn
from PIL import Image, ImageDraw, ImageFont


LOGO_LINKS            = ["https://telegra.ph/file/b51f91e129348f05a4ec5.jpg",
                          "https://telegra.ph/file/f313f05577ef9bcd3b0a7.jpg",
                          "https://telegra.ph/file/c921bdf4b7ada4398ac63.jpg",
                          "https://telegra.ph/file/a956a3e277e54adbaedfe.jpg",
                          "https://telegra.ph/file/01b1f61f9ee9e87255a36.jpg",
                          "https://telegra.ph/file/03f7cfe6f758981db4bd6.jpg",
                          "https://telegra.ph/file/bb22e2e6c4f274fd1ed52.jpg",
                          "https://telegra.ph/file/d04cb65453cec21fbb5b9.jpg",
                          "https://telegra.ph/file/ece9d497ab1906731d256.jpg",
                          "https://telegra.ph/file/06a694873ced962b023a8.jpg",
                          "https://telegra.ph/file/3df00b6def084a1f44e02.jpg",
                          "https://telegra.ph/file/7fd57d5431f47584f39e1.jpg",
                          "https://telegra.ph/file/72ed69b155a0aa1d44e04.jpg",
                          "https://telegra.ph/file/a3f312c6d5ec8eb25ab93.jpg",
                          "https://telegra.ph/file/833fada8cd50ba9dd97cc.jpg",
                          "https://telegra.ph/file/a209317e8b5c94449fb6e.jpg",
                          "https://telegra.ph/file/030cec0dc75107a740f1c.jpg",
                          "https://telegra.ph/file/e3f0cacf5e5fd9b13a238.jpg",
                          "https://telegra.ph/file/b3ac2f2b11ad918b5e8a8.jpg",
                          "https://telegra.ph/file/35acc3b54b670320ff26c.jpg",
                          "https://telegra.ph/file/0f73c41daf96635c6ab90.jpg", 
                          "https://telegra.ph/file/9492f0eac7494cc4f9ca0.jpg",
                          "https://telegra.ph/file/9492f0eac7494cc4f9ca0.jpg",
                          "https://telegra.ph/file/5283c51f51344ab3f10a7.jpg",
                          "https://telegra.ph/file/d9e132c40849037480bb8.jpg",
                          "https://telegra.ph/file/3424b69510d655af1b413.jpg",
                          "https://telegra.ph/file/fc5dcf0b2ebbc3cb65e34.jpg",
                          "https://telegra.ph/file/e3fd400e9645a99853a46.jpg",
                          "https://telegra.ph/file/4e239d14bf1e4794b0e62.jpg",
                          "https://telegra.ph/file/70789cd69114939a78242.jpg",
                          "https://telegra.ph/file/d4c8fe93d94534b7ab967.jpg",
                          "https://telegra.ph/file/e6a760b6b988e62be4e0c.jpg",
                          "https://telegra.ph/file/98237039c3069a7098fb5.jpg",
                          "https://telegra.ph/file/987915a5ac71b750b5807.jpg",
                          "https://telegra.ph/file/2d02972311802b998e36e.jpg",
                          "https://telegra.ph/file/e42968bdec3703cc3383b.jpg",
                          "https://telegra.ph/file/e6d61199273ba60e16915.jpg"
                        ]


@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id != OWNER_ID and not quew:
  await event.reply('`ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ ʙᴀʙʏ​ !`\n`Example /logo <Ankit>`')
  return
 pesan = await event.reply('**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ​...**')
 try:
    text = event.pattern_match.group(1)
    randc = random.choice(LOGO_LINKS)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "black"
    shadowcolor = "blue"
    fnt = glob.glob("./Ankit/resources/fonts/*")
    randf = random.choice(fnt)
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
    fname = "ankit.png"
    img.save(fname, "png")
    await telethn.send_file(event.chat_id, file=fname, caption = f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ᴘʀᴏᴊᴇᴄᴛ-x")         
    await pesan.delete()
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await event.reply(f'ғʟᴏᴏᴅᴡᴀɪᴛ ᴇʀʀᴏʀ, ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ @sassy_os')


__mod_name__ = "Lᴏɢᴏ​"

__help__ = """
Ankit can create some beautiful and attractive logo for your profile pics.

❍ /logo (Text) *:* Create a logo of your given text with random view.
"""
