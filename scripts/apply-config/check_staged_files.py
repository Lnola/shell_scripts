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


def get_config_entries(config_file: str):
    with open(config_file, "r") as f:
        mappings = json.load(f)
    return {Path(item["source"]).expanduser().resolve(): item for item in mappings}


def log_staged_and_config_files(staged_files, config_sources):
    print("Staged files:")
    if not staged_files:
        print("ℹ️ No staged files found.")
    for file in staged_files:
        print(f"- {file}")
    print("\nSources in .config.json:")
    if not config_sources:
        print("ℹ️ No sources found in .config.json.")
    for source in config_sources:
        print(f"- {source}")
    print()


def check_staged_files():
    config_map = get_config_entries(".config.json")
    config_sources = set(config_map.keys())
    staged_files = get_staged_files()

    log_staged_and_config_files(staged_files, config_sources)

    matching = [file for file in staged_files if file in config_sources]

    if not matching:
        return print("ℹ️ No staged files match sources in .config.json.")

    print("✅ Matching .config.json entries for staged files:")
    for file in matching:
        print(f"{json.dumps(config_map[file], indent=2)}\n")
    return [config_map[file] for file in matching]
