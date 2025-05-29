import json
import shutil
import subprocess
from pathlib import Path


def ask_user(prompt: str) -> bool:
    try:
        result = subprocess.run(
            [
                "osascript",
                "-e",
                f'display dialog "{prompt}" buttons {{"Cancel", "Yes"}} default button 2',
            ],
            capture_output=True,
            text=True,
        )
        return "Yes" in result.stdout
    except Exception as e:
        print(f"⚠️ Cannot ask user: {e}")
        return False


def show_diff(src: Path, dst: Path):
    try:
        subprocess.run(["code", "-d", str(dst), str(src)])
    except Exception as e:
        print(f"❌ Could not show diff: {e}")


def copy_files(mappings):
    for item in mappings:
        src = Path(item["source"]).expanduser().resolve()
        dst = Path(item["destination"]).expanduser().resolve()

        if not src.exists():
            print(f"❌ Source does not exist: {src}")
            continue

        if dst.exists():
            print(f"⚠️ {dst.name} already exists at destination.")
            show_diff(src, dst)
            if not ask_user(f"Overwrite {dst.name}?"):
                print("🚫 Skipped.")
                continue

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"✅ Copied {src} → {dst}")
