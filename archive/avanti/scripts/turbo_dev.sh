#!/bin/bash

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
            split vertically with default profile
        end tell

        # Split pane
        tell last session of current tab of current window
            split horizontally with default profile
        end tell

        # Run command in Pane-1
        tell first session of current tab of current window
            write text "z solution-tree-platform"
            write text "npm run dev:apps"
        end tell

        # Run command in Pane-2
        tell second session of current tab of current window
            write text "z solution-tree-platform"
            write text "npm run dev:server"
        end tell

        # Run command in Pane-4
        tell third session of current tab of current window
            write text "z solution-tree-platform"
        end tell

        # Focus Pane-4
        select third session of current tab of current window
    end tell
EOF
