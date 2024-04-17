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

osascript<<EOF
    tell application "Finder"
        set sel to the selection
        if (count sel) > 0 then
            set theFolder to item 1 of sel as alias
            return POSIX path of theFolder
        else
            if (count of Finder windows) > 0 then
                set theFolder to (target of front Finder window as alias)
                return POSIX path of theFolder
            else
                return "No Finder window open and no folder selected"
            end if
        end if
    end tell
EOF
