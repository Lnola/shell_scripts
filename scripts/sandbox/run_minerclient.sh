#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName MinerClient
# @raycast.title Run Miner
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 💎

# Documentation:
# @raycast.description Open the client for the Miner app.
# @raycast.author Luka Nola

SANDBOX=~/Sandboxes/MinerClient
HOME="$SANDBOX" java -Duser.home="$SANDBOX" -jar MinerClient.jar
