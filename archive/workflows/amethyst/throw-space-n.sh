#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Amethyst
# @raycast.title Throw space n
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../assets/amethyst.png
# @raycast.argument1 { "type": "text", "placeholder": "Number" }

# Documentation:
# @raycast.description Move the currently focused app to the nth space
# @raycast.author Luka Nola

# Get the AppleScript keycode from the argument
keycodes=( 18 19 20 21 23 22 26 28 25 )
keycode=${keycodes[$1 - 1]}

osascript<<EOF
    tell application "System Events" 
        key code $keycode using {shift down, option down, control down}
    end tell
EOF
