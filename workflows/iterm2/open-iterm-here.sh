#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Iterm2
# @raycast.title Keksi
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../assets/iterm.png

# Documentation:
# @raycast.description Open the current folder in Iterm2.
# @raycast.author Luka Nola

osascript<<EOF
    tell application "Finder"
        if (count of Finder windows) > 0 then
            set theFolder to (target of front Finder window as alias)
            return POSIX path of theFolder
        else
            return "No Finder window open"
        end if
    end tell
EOF
