import os
from nexa_userbot.core.main_cmd import nexaub_on_cmd, e_or_r

mod_file = os.path.basename(__file__)

@nexaub_on_cmd(command="hi", modlue=mod_file)
async def my_first_custom_plugin(client, message):
    await e_or_r(nexaub_message=message, msg_text="πΊβ¨β¨πΊβ¨πΊπΊπΊ\nπΊβ¨β¨πΊβ¨β¨πΊβ¨\nπΊπΊπΊπΊβ¨β¨πΊβ¨\nπΊβ¨β¨πΊβ¨β¨πΊβ¨\nπΊβ¨β¨πΊβ¨πΊπΊπΊ\nββββββββ\n")