#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Apply Hooks
# @raycast.title Apply Hooks
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🛠️

# Documentation:
# @raycast.description Apply hooks by copying ~/bin/hooks/ to ~/bin/.git/hooks
# @raycast.author Luka Nola

import shutil
from pathlib import Path


def apply_hooks():
    custom_hooks_dir = Path.home() / "bin/hooks"
    git_hooks_dir = Path.home() / "bin/.git/hooks"

    if not custom_hooks_dir.exists():
        print(f"Custom hooks directory not found: {custom_hooks_dir}")
        exit(1)

    if not git_hooks_dir.exists():
        print(f".git/hooks directory not found.")
        exit(1)

    for hook in custom_hooks_dir.iterdir():
        if hook.is_file():
            shutil.copy2(hook, git_hooks_dir / hook.name)
            print(f"Copied {hook.name} to .git/hooks/")


if __name__ == "__main__":
    apply_hooks()
