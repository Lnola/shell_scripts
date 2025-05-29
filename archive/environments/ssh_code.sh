#!/bin/bash

osascript<<EOF
    tell application "Visual Studio Code"
        activate
        delay 1
        tell application "System Events"
            key down command
            keystroke "p"
            key up command
            keystroke ">Remote-SSH: Connect Current Window to Host"
            delay 1
            key code 36
            delay 1
            keystroke "localhost"
            delay 1
            key code 36
        end tell
    end tell
EOF
