#!/usr/bin/env python3
import os, yaml, re

mod_pattern = r'^mod[1-4]'

home_dir = os.environ['HOME']
config_file_path = f"{home_dir}/.amethyst.yml"

modifiers_mapping = {}

key_codes = {
    'enter': 36,
    'return': 36,
    'space': 49,
    'left': 123,
    'right': 124,
    'down': 125,
    'up': 126,
    '1': 18,
    '2': 19,
    '3': 20,
    '4': 21,
    '5': 23,
    '6': 22,
    '7': 26,
    '8': 28,
    '9': 25,
}

script_template = """#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Amethyst
# @raycast.title {title}
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ./assets/amethyst.png

# Documentation:
# @raycast.description Amethyst shortcut generated by generate_scripts.py
# @raycast.author Luka Nola

tell application "System Events"
    {key} using {{{mod}}}
end tell
"""

def load_yaml_config(file_path):
    """Load and return YAML configuration from a file."""
    try:
        with open(file_path, "r") as file:
            config_data = yaml.safe_load(file)
            if config_data is None:
                print("The configuration file is empty or incorrectly formatted.")
                exit(3)
            return config_data

    except FileNotFoundError:
        print(f"Error: Config file not found at {file_path}. Exiting.")
        exit(1)

    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}. Exiting.")
        exit(2)


def format_title(name):
    """Convert snake_case or kebab-case to Title Case."""
    return name.replace('-', ' ').replace('_', ' ').title().replace(' Ccw', ' CCW').replace(' Cw', ' CW')


def generate_applescript_commands(modifier, key):
    """Generate AppleScript commands from modifiers and key."""
    if modifier not in modifiers_mapping:
        raise ValueError(f"Invalid modifier: {modifier}")
    mod = ', '.join([f"{mod_key} down" for mod_key in modifiers_mapping[modifier]])
    
    if len(key) == 1:
        key = f'keystroke "{key}"'
    elif key in key_codes:
        key = f'key code {key_codes[key]}'
    else:
        raise ValueError(f"Invalid key: {key}")
    
    return mod, key


def generate_script(file_path, title, mod, key):
    """Generate AppleScript based on the template and write to the file."""
    script_content = script_template.format(title=title, key=key, mod=mod)
    with open(file_path, 'w') as script_file:
        script_file.write(script_content)


def generate_scripts(command, keybind):
    try:
        title = format_title(command)
        mod, key = generate_applescript_commands(keybind['mod'], keybind['key'])
        script_path = f"{command}.applescript"
        generate_script(script_path, title, mod, key)
        print(f"Generated script: {script_path}")
    except ValueError as error:
        print(f"Skipping '{command}': {error}")


def main():
    config_data = load_yaml_config(config_file_path)

    for key, value in config_data.items():
        # map modifiers mod[1-4]
        if re.match(mod_pattern, key):
            modifiers_mapping[key] = value

        # generate scripts for keybindings
        if isinstance(value, dict):
            generate_scripts(key, value)

if __name__ == "__main__":
    main()
