#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Apply Config
# @raycast.title Apply Config
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🛠️
# @raycast.argument1 { "type": "text", "placeholder": "Apply all (y/n)" }

# Documentation:
# @raycast.description Apply configuration by copying files from source to destination.
# @raycast.author Luka Nola

import json, argparse
from pathlib import Path
from check_staged_files import check_staged_files
from copy_file_to_destination import copy_files


def read_config(config_file: str):
    with open(config_file, "r") as f:
        mappings = json.load(f)
    return mappings


def build_config(args):
    if args.apply_all and args.apply_all.lower() == "y":
        config_file_path = Path(__file__).resolve().parent / ".config.json"
        return read_config(config_file_path)

    return check_staged_files()


def apply_config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "apply_all",
        type=str,
        help="Apply all (y/n)",
        nargs="?",
    )
    args = parser.parse_args()

    config = build_config(args)
    copy_files(config)


if __name__ == "__main__":
    apply_config()
