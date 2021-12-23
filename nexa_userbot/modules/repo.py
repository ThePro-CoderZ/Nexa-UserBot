import os
from nexa_userbot.core.main_cmd import nexaub_on_cmd, e_or_r

mod_file = os.path.basename(__file__)

@nexaub_on_cmd(command="repo", modlue=mod_file)
async def my_first_custom_plugin(client, message):
    await e_or_r(nexaub_message=message, msg_text="[]Nexa Userbot[]\n\nRepository》[Here](https://github.com/ThePro-CoderZ/Nexa-Userbot)\nString Session》[Here](https://repl.it/@AkshatKumar6/String-Nexa)\nSupport》[Group](https://t.me/TheArjvpsChat)\nSupport》[Channel](https://t.me/TheArjvps)\n\nThis is the Best Userbot to Manager your Telegram Account!")