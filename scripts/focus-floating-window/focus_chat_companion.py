#!/usr/bin/env python3
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
cx = (x0 + x1) // 2
cy = (y0 + y1) // 2

subprocess.run(["/opt/homebrew/bin/cliclick", f"c:{cx},{cy}"], check=True)
