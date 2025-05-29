#!/bin/bash

# Get the AppleScript keycode from the argument
keycodes=( 18 19 20 21 23 22 26 28 25 )
keycode=${keycodes[$1 - 1]}

osascript<<EOF
    tell application "System Events" 
        key code $keycode using {control down}
    end tell
EOF
