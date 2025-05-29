#!/bin/bash

osascript<<EOF
tell application "iTerm"
        activate
        select first window

        tell first session of current tab of current window
            write text ""
            write text ""
        end tell

        tell second session of current tab of current window
            write text ""
            write text ""
        end tell

        tell current tab of current window
            close
        end tell
    end tell
EOF

