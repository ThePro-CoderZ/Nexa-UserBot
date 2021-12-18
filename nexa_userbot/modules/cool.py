import os
from nexa_userbot.core.main_cmd import nexaub_on_cmd, e_or_r


# Help
CMD_HELP.update(
    {
        "cool": f"""
**Cool,**
  ✘ `cool` - To send "I'm Cool"
"""
    }
)

mod_file = os.path.basename(__file__)

@nexaub_on_cmd(command="cool", modlue=mod_file)
async def my_first_custom_plugin(client, message):
    await e_or_r(nexaub_message=message, msg_text="`I'm Cool!`")
