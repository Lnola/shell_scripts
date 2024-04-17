#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Iterm2
# @raycast.title Open iTerm Here
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../assets/iterm.png

# Documentation:
# @raycast.description Open the current folder in Iterm2.
# @raycast.author Luka Nola

import subprocess


# AppleScript to get the selected or current folder path from Finder or ""
finder_script = """
    tell application "Finder"
        set sel to the selection
        if (count sel) > 0 then
            return POSIX path of (item 1 of sel as alias)
        else if (count of Finder windows) > 0 then
            return POSIX path of (target of front Finder window as alias)
        else
            return ""
        end if
    end tell
"""

# AppleScript for opening iTerm2 and executing commands
iterm_script = """
tell application "iTerm"
    create window with default profile
    tell current session of current window
        write text "cd '{path}'"
        write text "clear"
    end tell
end tell
"""


def execute_applescript(script, **script_args):
    """Executes AppleScript, substituting in any keyword arguments provided."""
    script = script.format(**script_args)
    process = subprocess.run(
        ["osascript", "-e", script], text=True, capture_output=True
    )
    return process.stdout.strip()


def main():
    folderPath = execute_applescript(finder_script)
    
    if folderPath:
        execute_applescript(iterm_script, path=folderPath)
    else:
        print("No Finder window open and no folder selected")


if __name__ == "__main__":
    main()
