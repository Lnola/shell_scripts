#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Workflows
# @raycast.title avanti
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ./assets/avanti.png

# Documentation:
# @raycast.description Start avanti workflow
# @raycast.author Luka Nola


osascript<<EOF
    tell application "Arc" to activate
    tell application "Slack" to activate
    tell application "Spotify" to activate
    tell application "Iterm" to activate

    delay 2

    do shell script "utils/move_app_to_space.sh Spotify 1"
    do shell script "utils/move_app_to_space.sh Slack 2"
    do shell script "utils/move_app_to_space.sh Iterm 5"

    delay 1

    do shell script "utils/move_app_to_space.sh Arc 3"

    delay 1

    tell application "Iterm"
        activate
        write text "z sol && code ."

        # Split pane
        tell current session of current window
            split vertically with default profile
        end tell

        # Split pane
        tell current session of current window
            split horizontally with default profile
        end tell

        tell first session of current tab of current window
            write text "z learn"
            write text "npm run storybook:dev"
        end tell

        tell second session of current tab of current window
            write text "z learn"
            write text "npm run dev"
        end tell

        tell third session of current tab of current window
            write text "z learn && code ."
        end tell
    end tell
EOF
