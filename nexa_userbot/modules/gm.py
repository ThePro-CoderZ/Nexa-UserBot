import os
from nexa_userbot.core.main_cmd import nexaub_on_cmd, e_or_r

mod_file = os.path.basename(__file__)

@nexaub_on_cmd(command="gm", modlue=mod_file)
async def my_first_custom_plugin(client, message):
    await e_or_r(nexaub_message=message, msg_text="Good Mᴏʀɴiɴɢ\n\nNᴏ ᴍᴀᴛᴛᴇʀ ᕼᴏᴡ ɢᴏᴏᴅ ᴏʀ\nʙᴀᴅ ʏᴏᴜʀ ʟiғᴇ is,\nᴡᴀᴋᴇ ᴜᴘ ᴇᴀᴄᕼ ᴍᴏʀɴiɴɢ\nᴀɴᴅ ʙᴇ ᴛᕼᴀɴᴋғᴜʟ\nYᴏᴜ sᴛiʟʟ ᕼᴀᴠᴇ ᴀ ɴᴇᴡ ᴅᴀʏ.\n\n        🌞\n         ╱◥████◣\n│田│▓ ∩│◥███◣\n╱◥◣ ◥████◣田∩田│\n│╱◥█◣║∩∩∩ 田∩田│\n║◥███◣∩田∩ 田∩田│\n│∩│ ▓ ║∩田│║▓田▓\n🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹")