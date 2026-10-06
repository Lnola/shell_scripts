---
name: yabai-config
description: Use when changing this user's yabai or skhd settings, window-management shortcuts, tiling behavior, .yabairc, or .skhdrc. Apply the changes yourself by editing the canonical configs in ~/bin/config first, copying changed files to the home directory, and restarting both services. Keep SIP enabled.
---

# Configure yabai and skhd

Carry out the requested changes rather than handing the user code to paste. The
user maintains their configs in `~/bin`; the home-directory files are deployed
copies. Follow this order: **edit source → copy → restart both → verify**.

## File mapping

| Canonical source | Deployed copy |
| --- | --- |
| `~/bin/config/yabai/.yabairc` | `~/.yabairc` |
| `~/bin/config/skhd/.skhdrc` | `~/.skhdrc` |

Use `$HOME` or resolved absolute paths; do not assume the current directory is
the home directory. Keep these as copied files, not symlinks.

## Workflow

1. **Inspect before editing.** Read the relevant canonical and deployed files,
   plus applicable repository instructions. Check existing bindings and rules
   so the requested change does not duplicate or unexpectedly replace them.
   If the deployed copy contains additional user changes, preserve them in the
   canonical file before copying. Ask only when conflicting changes make the
   intended result unclear. Respect existing staged and unstaged Git changes.

2. **Check command behavior when needed.** Use the official yabai GitHub docs,
   and the skhd GitHub docs for hotkey syntax and service commands. Check the
   installed version when a feature's availability is uncertain. Prefer
   Homebrew for package management if installation or an upgrade is requested.

3. **Edit the canonical file first.** Make only the requested changes in
   `~/bin/config/yabai/.yabairc` and/or `~/bin/config/skhd/.skhdrc`. Preserve
   unrelated settings. Do not edit only the home-directory copy. For changes to
   `.yabairc`, run `sh -n` against the source before deploying; this checks shell
   syntax, not whether yabai supports each option.

4. **Copy each changed source to its deployed path.** After editing, run the
   applicable commands below. Copy only files involved in the change, and
   finish all copies before restarting services.

   ```sh
   cp "$HOME/bin/config/yabai/.yabairc" "$HOME/.yabairc"
   cp "$HOME/bin/config/skhd/.skhdrc" "$HOME/.skhdrc"
   ```

   Verify each deployed file matches its source with `cmp -s`. Stop and resolve
   a copy or comparison failure before proceeding.

5. **Restart both services, even if only one config changed.** Execute these in
   the terminal after deployment; a config reload alone does not fulfill the
   user's workflow.

   ```sh
   yabai --restart-service
   skhd --restart-service
   ```

   Resolve the binaries with `command -v` if they are not available on PATH.
   On this Apple Silicon Homebrew setup they have been installed under
   `/opt/homebrew/bin`. If a restart fails, diagnose and report the failure
   rather than claiming both services restarted successfully.

6. **Verify and summarize.** Confirm both processes remain running and yabai
   responds to a read-only query such as `yabai -m query --spaces --space`.
   When inspecting launchd, obtain the service label from the installed plist
   in `~/Library/LaunchAgents`; releases may use either `com.asmvik.*` or
   `com.koekeishiya.*`. Inspect service errors only if needed and permitted.
   Report the changed source and deployed paths, the shortcuts/settings added,
   and the restart results. Distinguish service checks from actual keypress
   testing. Do not commit or push unless asked.

## User's standing preferences

- **Keep System Integrity Protection (SIP) enabled.** Do not disable or weaken
  SIP, modify boot arguments, configure passwordless sudo, or load yabai's
  scripting addition. If a requested feature requires those changes, explain
  the limitation and look for a SIP-compatible way to achieve the goal.
- Preserve existing personal shortcuts unless the user requests a change.
- Follow the keyboard conventions in `~/bin/AGENTS.md`. Read the canonical
  config files for current bindings, settings, and inline explanations. Keep
  shortcut-specific documentation alongside the bindings; do not duplicate a
  shortcut inventory in this skill or `AGENTS.md`.
- A request for advice or inspection alone is not permission to deploy changes
  or restart services. For an actual configuration-change request, perform the
  complete workflow without making the user write or copy the code themselves.

## Official references

- [yabai configuration](https://github.com/asmvik/yabai/wiki/Configuration)
- [yabai command reference](https://github.com/asmvik/yabai/blob/master/doc/yabai.asciidoc)
- [yabai installation and service setup](https://github.com/asmvik/yabai/wiki/Installing-yabai-(latest-release))
- [skhd syntax and service commands](https://github.com/asmvik/skhd)
