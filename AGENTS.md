# Agent Instructions For ~/bin

## Repository Scope

This is a personal macOS tooling repository. It contains canonical shell and app
configuration under `config/`, Python and shell utilities under `scripts/`, Git
hooks under `hooks/`, assets, and retired workflows under `archive/`. The
`README.md` is explicitly outdated; inspect the relevant source instead of
treating it as current documentation.

## Editing And Deployment

- Treat files in `config/` as the editable source for managed dotfiles. Deployed
  home-directory files are copies, not symlinks.
- The local, ignored `scripts/apply-config/.config.json` defines source-to-
  destination mappings. Use `.config.example.json` as its shareable template.
- `scripts/apply-config/apply_config.py` deploys either all mappings when given
  `y`, or only mappings for staged files. It prompts before overwriting an
  existing destination.
- `hooks/pre-commit` invokes that script through the user's Python virtual
  environment when Git's `core.hooksPath` is set to `hooks`.
- Preserve existing staged, unstaged, and untracked work. Do not assume every
  configuration file is installed or that the optional hook is enabled.

## Scripts And Environment

- Most Python utilities are Raycast scripts and include their Raycast metadata
  at the top of the file. Preserve the expected interpreter and metadata when
  editing them.
- These tools target macOS and may depend on AppleScript, Finder, Homebrew
  binaries, installed applications, and user-specific paths. Check a dependency
  before relying on it; do not introduce portability shims unless requested.
- `config/zsh/.zshrc` sources `~/.zsh_alias`, `~/.zsh_env`, and
  `~/.starship.zsh`. Keep related environment and shell changes consistent with
  those deployed paths.

## Verification

- For Python edits, run an appropriate syntax or targeted execution check when
  its macOS dependencies do not make that unsafe. For shell edits, use a shell
  syntax check where applicable.
- Review the relevant configuration mapping and diff after changes. Deployment
  and service restarts require explicit workflow support; do not run unrelated
  personal automation merely because a file changed.

## Yabai And Skhd

For yabai or skhd changes, load `.agents/skills/yabai-config/SKILL.md` before
editing. It owns the canonical-to-deployed file mappings and the required
edit, copy, restart, and verification workflow. Keep System Integrity
Protection enabled.

- Use **Ctrl + Option** for the base shortcut group.
- Add **Shift** for alternate actions: **Ctrl + Option + Shift**.
- Keep directions on the split keyboard home row: **J = left, K = down, L = up,
  ; = right**.
- Read `config/skhd/.skhdrc` and `config/yabai/.yabairc` for current bindings,
  settings, and inline explanations. Do not maintain a shortcut inventory here.
