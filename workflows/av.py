#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Workflows
# @raycast.title av
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon ./assets/avanti.png

# Documentation:
# @raycast.description Start avanti workflow
# @raycast.author Luka Nola

import subprocess
import time
import psutil


# Function to check if an application is running
def app_is_running(app_name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == app_name:
            return True
    return False


# Function to wait until an application is running
def wait_for_app_to_launch(app_name, max_wait=5):
    elapsed_time = 0
    while elapsed_time < max_wait:
        if app_is_running(app_name):
            return True
        time.sleep(1)
        elapsed_time += 1
    return False


print("Starting the script")

# Activate applications
subprocess.run(["open", "-a", "Arc"])
wait_for_app_to_launch("Arc")

subprocess.run(["open", "-a", "Slack"])
wait_for_app_to_launch("Slack")

subprocess.run(["open", "-a", "Spotify"])
wait_for_app_to_launch("Spotify")

subprocess.run(["open", "-a", "iTerm"])
wait_for_app_to_launch("iTerm")


print("Opened apps, moving them to the correct spaces")

# # Move applications to spaces
subprocess.run(["utils/move_app_to_space.sh", "Spotify", "1"])
subprocess.run(["utils/move_app_to_space.sh", "Slack", "2"])
subprocess.run(["utils/move_app_to_space.sh", "Arc", "3"])
subprocess.run(["utils/move_app_to_space.sh", "iTerm", "5"])

time.sleep(1)

subprocess.run(["arc/switch_space.sh", "2"])

# time.sleep(1)

# # Open iTerm and execute commands
# subprocess.run(
#     [
#         "osascript",
#         "-e",
#         """
# tell application "iTerm"
#     activate
#     tell current session of current window to write text "z sol && code ."
#     tell application "System Events" to keystroke "avst"
#     delay 1
#     activate
# end tell
# """,
#     ]
# )
