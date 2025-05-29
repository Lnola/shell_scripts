#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Sign Contract
# @raycast.title Sign Contract
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 📁

# Documentation:
# @raycast.description Signs the contract currently selected in Finder
# @raycast.author Luka Nola


from sign_pdf import sign_pdf
import subprocess


def get_selected_file_path():
    script = """
    tell application "Finder"
        set selectedFiles to selection
        if (count of selectedFiles) is greater than 0 then
            set theFile to item 1 of selectedFiles
            set theFilePath to POSIX path of (theFile as alias)
            return theFilePath
        else
            return "No file selected."
        end if
    end tell
    """

    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip()


if __name__ == "__main__":
    file_path = get_selected_file_path()
    if file_path == "No file selected.":
        print("No file selected. Please select a file in Finder.")
    else:
        print(file_path)
        print(f"Selected file path: {file_path}")
        # Call the global script
        sign_pdf(file_path)
