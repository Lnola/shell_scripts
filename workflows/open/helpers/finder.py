# AppleScript to get the selected or current folder path from Finder or ""
finder_script = """
    tell application "Finder"
        set sel to the selection
        if (count sel) > 0 then
            return POSIX path of (item 1 of sel as alias)
        else if (count of Finder windows) > 0 then
            return POSIX path of (target of front Finder window as alias)
        else
            return ""
        end if
    end tell
"""
