# Copyright (c) 2021 ThePro-CoderZ
# Part of: Nexa-Userbot
import os

from pyrogram import filters
from pyrogram.types import Message
from datetime import datetime

from nexa_userbot import NEXAUB, CMD_HELP
from nexa_userbot.core.nexaub_database.nexaub_db_afk import me_afk, get_afk, me_online
from nexa_userbot.core.main_cmd import nexaub_on_cmd, e_or_r, nexaub_on_cf
from nexa_userbot.helpers.pyrogram_help import get_arg
from config import Config


# Help
CMD_HELP.update(
    {
        "std": f"""
**Afk,**
  ✘ `std` - To Activate Study Module
**Example:**
  ✘ `std`,
   ⤷ Send with reason = `{Config.CMD_PREFIX}std` Exam\Test
"""
    }
)

mod_file = os.path.basename(__file__)

# Check if Studing!
async def u_afk_bro(filter, client, message):
    if_std = await get_std()
    if if_std:
        return True
    else:
        return False

# Creating a custom filter
ya_std = filters.create(func=u_std_bro, name="is_ya_std")


@nexaub_on_cmd(command="std", modlue=mod_file)
async def me_goin_oflin(_, message: Message):
    std_msg = await e_or_r(nexaub_message=message, msg_text="`Processing...`")
    std_reason = get_arg(message)
    if not std_reason:
        std_reason = "I'm Bust in Study! Will Come Online Later :)"
    std_time = datetime.now().replace(microsecond=0)
    await me_std(std_time=std_time, std_reason=std_reason)
    await std_msg.edit(f"**I'm Going to study** \n\n**Reason:** `{afk_reason}`")

@nexaub_on_cf(
    ya_std
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.edited
    & filters.incoming)
async def me_std_tho(_, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    s_time, a_reason = await get_std()
    now_time = datetime.now().replace(microsecond=0)
    std_time = str((now_time - s_time))
    await message.reply(f"**I'm Studing** \n\n**Last Online:** `{std_time}` \n**Reason:** `{a_reason}`")

@nexaub_on_cf(
    filters.me
    & filters.outgoing
    & ya_std
)
async def back_online_bois(_, message: Message):
    s_time, a_reason = await get_std()
    com_online = datetime.now().replace(microsecond=0)
    afk_time = str((com_online - s_time))
    await me_online()
    await e_or_r(nexaub_message=message, msg_text=f"**I'm No Longer Studing** \n\n**Study For Time:** `{afk_time}` \n**Why?:** `{a_reason}`")
