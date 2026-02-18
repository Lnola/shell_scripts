#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName GitFlab
# @raycast.title PR Commits
# @raycast.mode silent
# @raycast.argument1 { "type": "text", "placeholder": "Parent branch (default: staging)", "optional": true }
# @raycast.argument2 { "type": "text", "placeholder": "Child branch (default: current)", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "Repository path (default: current)", "optional": true }

# Optional parameters:
# @raycast.icon 🌳

# Documentation:
# @raycast.description Generate a formatted list of commits for a PR and copy to clipboard
# @raycast.author Luka Nola

import subprocess
import sys
import os

parent = (
    (sys.argv[1].strip() if sys.argv[1].strip() else "staging")
    if len(sys.argv) > 1
    else "staging"
)
child = (
    (sys.argv[2].strip() if sys.argv[2].strip() else None)
    if len(sys.argv) > 2
    else None
)
repo_path = (
    (
        sys.argv[3].strip()
        if sys.argv[3].strip()
        else os.path.expanduser("~/Projects/skeleton-go")
    )
    if len(sys.argv) > 3
    else os.path.expanduser("~/Projects/skeleton-go")
)


def run_git(args):
    """Run git command in the specified repository"""
    cmd = ["git", "-C", repo_path] + args
    env = os.environ.copy()
    env["LANG"] = "en_US.UTF-8"
    env["LC_ALL"] = "en_US.UTF-8"
    return subprocess.check_output(cmd, text=True, encoding="utf-8", env=env).strip()


if not child:
    child = run_git(["rev-parse", "--abbrev-ref", "HEAD"])

merge_base = run_git(["merge-base", parent, child])

commits = run_git(["log", f"{merge_base}..{child}", "--format=* %s"])

output = "\n\n".join(commits.splitlines())

# Use osascript to copy to clipboard with proper UTF-8 handling
script = f'set the clipboard to "{output.replace(chr(34), chr(92) + chr(34))}"'
subprocess.run(["osascript", "-e", script], check=True)
print(f"Copied {len(commits.splitlines())} commits to clipboard")
