# Copyright (c) 2021 ThePro-CoderZ
# Part of: Nexa-Userbot

import glob
from os.path import dirname, basename, isfile, join

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]

# Telegram IDs of ub dev(s)
nexaub_devs = [1883911756]
