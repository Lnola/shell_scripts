#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Throw space n
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ./assets/amethyst.png
# @raycast.argument1 { "type": "text", "placeholder": "Number" }

# Documentation:
# @raycast.description Move the currently focused app to the nth space
# @raycast.author Luka Nola

"../utils/move_app_to_space_n.sh" "$1"

