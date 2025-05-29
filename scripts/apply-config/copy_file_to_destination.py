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

import json
import shutil
from pathlib import Path


def copy_files(mapping_file):
    with open(mapping_file, "r") as f:
        mappings = json.load(f)

    for item in mappings:
        src = Path(item["source"]).expanduser().resolve()
        dst = Path(item["destination"]).expanduser().resolve()

        if not src.exists():
            print(f"❌ Source does not exist: {src}")
            continue

        dst.parent.mkdir(parents=True, exist_ok=True)  # Ensure target dir exists
        shutil.copy2(src, dst)  # copy2 preserves metadata
        print(f"✅ Copied {src} → {dst}")


if __name__ == "__main__":
    copy_files(".config.json")
