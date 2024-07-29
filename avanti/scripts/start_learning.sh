#!/bin/bash

keycodes=( 18 19 20 21 23 22 26 28 25 )
keycode=${keycodes[4 - 1]}

osascript<<EOF
    tell application "Iterm"
        activate      

        # Create new tab
        tell current window
            create tab with default profile
        end tell  

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
            write text "z learn"
            # write text "z learn && code ."
        end tell
    end tell

    delay 1

    # tell application "System Events" 
    #     key code $keycode using {shift down, option down, control down}
    # end tell
EOF

