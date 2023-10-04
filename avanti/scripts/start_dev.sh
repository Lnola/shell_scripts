# !/bin/bash

osascript<<EOF
    tell application "iTerm"
        activate
        select first window

        # Create new tab
        tell current window
            create tab with default profile
        end tell

        # Split pane
        tell current session of current window
            split horizontally with default profile
        end tell

        # Split pane
        tell current session of current window
            split vertically with default profile
        end tell

        # Start test postgres in Pane-3
        tell third session of current tab of current window
            write text "z sol"
            write text "av pg:kill:test"
            write text "av pg:start:dev"
        end tell

         # Wait for postgres to start before starting the apps
        set var_wait to 0
        repeat until (var_wait = 1)
            if (text of third session of current tab of current window contains "avanti_postgres") then
                set var_wait to 1
            end if
        end repeat

        # Run command in Pane-1
        tell first session of current tab of current window
            write text "z sol"
            write text "npm run dev:server"
        end tell

        # Run command in Pane-2
        tell second session of current tab of current window
            write text "z sol"
            write text "npm run dev:client"
        end tell

        # # Write start of test command in Pane-3
        # tell third session of current tab of current window
        #     write text "code ."
        # end tell
        
        # Focus Pane-3
        select third session of current tab of current window
    end tell
EOF
