#!/Users/lnola/.python/python-venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Open
# @raycast.title Open iTerm Here
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../../assets/icons/iterm.png

# Documentation:
# @raycast.description Open the current folder in Iterm2.
# @raycast.author Luka Nola

from scripts.utils.execute_applescript import execute_applescript
from finder import finder_script


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


def main():
    folderPath = execute_applescript(finder_script)

    if folderPath:
        execute_applescript(iterm_script, path=folderPath)
    else:
        print("No Finder window open and no folder selected")


if __name__ == "__main__":
    main()
