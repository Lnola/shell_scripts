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
            write text "ssh root@localhost -p 2222"
            # Clone the repository
            write text "git clone git@github.com:Lnola/College.git"

            #  Wait for Command + D
            set var_wait to 0
            repeat until (var_wait = 1)
                if (text of current session of current window contains "Connection to localhost closed.") then
                    set var_wait to 1
                end if
            end repeat

            # Stop the docker container
            write text "(z python && docker compose stop)"
        end tell
    end tell
EOF
