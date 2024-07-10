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


# Function to wait until all applications in the list are running
def wait_for_apps_to_launch(app_names, max_wait=5):
    start_time = time.time()
    while time.time() - start_time < max_wait:
        remaining_apps = [app for app in app_names if not app_is_running(app)]
        if not remaining_apps:
            print(f"All applications are running: {', '.join(app_names)}")
            return True
        time.sleep(1)
    print(f"Failed to start all applications: {', '.join(remaining_apps)}")
    return False


print("Starting the script")

# Activate applications
subprocess.run(["open", "-a", "Arc"])
subprocess.run(["open", "-a", "Slack"])
subprocess.run(["open", "-a", "Spotify"])
subprocess.run(["open", "-a", "iTerm"])

# List of applications to wait for
apps_to_launch = ["Arc", "Slack", "Spotify", "iTerm2"]
wait_for_apps_to_launch(apps_to_launch)


time.sleep(1)

# subprocess.run(["arc/switch_space.sh", "2"])

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
