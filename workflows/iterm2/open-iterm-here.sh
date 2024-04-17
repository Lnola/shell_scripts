#!/bin/bash

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

# Run AppleScript to get the current or selected folder path from Finder
folderPath=$(
osascript<<EOF
    tell application "Finder"
        set sel to the selection
        # Check if a folder is selected and return its path
        if (count sel) > 0 then
            return POSIX path of (item 1 of sel as alias)
        # Check if a folder is open and return its path
        else if (count of Finder windows) > 0 then
            return POSIX path of (target of front Finder window as alias)
        # Return an empty string if no folder is open or selected
        else
            return ""
        end if
    end tell
EOF
)

# Check if the path was returned
if [ -n "$folderPath" ]; then
    # Open iTerm2 and execute cd command to navigate to the folder
    osascript -e "tell application \"iTerm\"
            create window with default profile
            tell current session of current window
                write text \"cd $folderPath\"
                write text \"clear\"
            end tell
        end tell"
else
    # Print an error message if the path is empty
    echo "No Finder window open and no folder selected"
fi
