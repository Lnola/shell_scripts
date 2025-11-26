#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Focus
# @raycast.title Focus Chat Companion
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🖱️

# Documentation:
# @raycast.description Focus the Chat Companion text input.
# @raycast.author Luka Nola

import subprocess

bounds = (
    subprocess.check_output(
        [
            "osascript",
            "-e",
            'tell application "Finder" to get bounds of window of desktop',
        ],
        text=True,
    )
    .strip()
    .split(", ")
)

x0, y0, x1, y1 = map(int, bounds)
cx = x1 - 1600
cy = y1 - 160

subprocess.run(["/opt/homebrew/bin/cliclick", f"c:{cx},{cy}"], check=True)
