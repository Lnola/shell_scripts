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
import subprocess
from pathlib import Path


def get_staged_files():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "--cached"],
            capture_output=True,
            text=True,
            check=True,
        )
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        return [
            (BASE_DIR / line.strip()).resolve() for line in result.stdout.splitlines()
        ]
    except subprocess.CalledProcessError:
        print("❌ Error running git diff. Are you in a git repo?")
        return []


def get_config_sources(config_file: str):
    with open(config_file, "r") as f:
        mappings = json.load(f)
    return [Path(item["source"]).expanduser().resolve() for item in mappings]


def log_staged_and_config_files(staged_files, config_sources):
    print("Staged files:")
    for file in staged_files:
        print(f"- {file}")
    print("\nSources in .config.json:")
    for source in config_sources:
        print(f"- {source}")


def main():
    config_sources = set(get_config_sources(".config.json"))
    staged_files = get_staged_files()
    log_staged_and_config_files(staged_files, config_sources)

    matching = [str(file) for file in staged_files if file in config_sources]

    if not matching:
        return print("ℹ️ No staged files match sources in .config.json.")

    print("✅ Staged files found in .config.json:")
    for f in matching:
        print(f"- {f}")


if __name__ == "__main__":
    main()
