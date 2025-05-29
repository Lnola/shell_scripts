#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Apply Config
# @raycast.title Apply Config
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🛠️

# Documentation:
# @raycast.description Apply configuration by copying files from source to destination.
# @raycast.author Luka Nola

from check_staged_files import check_staged_files
from copy_file_to_destination import copy_files


def apply_config():
    config = check_staged_files()
    copy_files(config)


if __name__ == "__main__":
    apply_config()
