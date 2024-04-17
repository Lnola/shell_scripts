#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Open VSCode
# @raycast.title Open VSCode Here
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../assets/vscode.png

# Documentation:
# @raycast.description Open the current folder in Visual Studio Code.
# @raycast.author Luka Nola

from helpers.execute_applescript import execute_applescript

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

# AppleScript for opening Visual Studio Code in the specified directory
vscode_script = """
    tell application "Visual Studio Code"
        activate
        open POSIX file "{path}"
    end tell
"""


def main():
    folderPath = execute_applescript(finder_script)

    if folderPath:
        execute_applescript(vscode_script, path=folderPath)
    else:
        print("No Finder window open and no folder selected")


if __name__ == "__main__":
    main()
