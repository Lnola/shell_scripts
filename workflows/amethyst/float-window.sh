#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Amethyst
# @raycast.title Float window
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../assets/amethyst.png

# Documentation:
# @raycast.description Make the currently selected window float and reduce the size
# @raycast.author Luka Nola

# Before running the command make sure to install Rectangle and set
# Almost maximize: control + shift + option + = 
# Make smaller: control + shift + option + -

osascript<<EOF
    tell application "System Events"
        key code 24 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
        key code 27 using {option down, shift down, control down}
    end tell
EOF
