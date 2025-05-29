#!/Users/lnola/.python/python-venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Open
# @raycast.title Open VSCode Here
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../../assets/icons/vscode.png

# Documentation:
# @raycast.description Open the current folder in Visual Studio Code.
# @raycast.author Luka Nola

from scripts.utils.execute_applescript import execute_applescript
from helpers.finder import finder_script


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
