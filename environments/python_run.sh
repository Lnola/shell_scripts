# !/bin/bash

osascript<<EOF
    tell application "iTerm"
        activate
        select first window

        # Create new tab
        tell current window
            create tab with default profile
        end tell

        tell current session of current window
            # Start the docker container
            write text "(z python && docker compose up -d)"
            # SSS into the docker container
            write text "ssh eedev@localhost -p 2222"
        end tell

        #  Wait for Command + D
        set var_wait to 0
        repeat until (var_wait = 1)
            if (text of current session of current window contains "Connection to localhost closed.") then
                set var_wait to 1
            end if
        end repeat

        tell current session of current window
            # Stop the docker container
            write text "(z python && docker compose stop)"
        end tell
    end tell
EOF
