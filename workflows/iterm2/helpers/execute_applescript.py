def execute_applescript(script, **script_args):
    """Executes AppleScript, substituting in any keyword arguments provided."""
    import subprocess
    script = script.format(**script_args)
    process = subprocess.run(["osascript", "-e", script], text=True, capture_output=True)
    return process.stdout.strip()
