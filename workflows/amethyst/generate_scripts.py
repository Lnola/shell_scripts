#!/usr/bin/env python3
import os, yaml

home_dir = os.environ['HOME']
config_file_path = f"{home_dir}/.amethyst.yml"
mod1 = ['option', 'shift']
mod2 = ['option', 'shift', 'control']
keycodes = {
    'enter': 36,
    'return': 36,
    'space': 49,
    'left': 123,
    'right': 124,
    'down': 125,
    'up': 126,
}

script_template = """#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Amethyst
# @raycast.title Generate amethyst scripts
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ./assets/amethyst.png
# @raycast.author Luka Nola
# @raycast.description Keyboard shortcuts automatic generator from config .amethyst.yml

tell application "System Events" 
    <<command>> using {<<mods>>}
end tell
"""

# mod1|mod2 -> option down, shift down
def mods_csv(mod):
    if mod != 'mod1' and mod != 'mod2':
        raise ValueError(f"invalid mod: {mod}")

    mods = mod1 if mod == 'mod1' else mod2
    return ', '.join([f"{mod} down" for mod in mods])


# h, j, k, l, space, return, left, right -> keystroke "h" | key code 49
def key_cmd(key):
    if len(key) == 1:
        return f"keystroke \"{key}\""
    elif key in keycodes:
        code = keycodes[key]
        return f"key code {code}"
    else:
        raise ValueError(f"invalid key: {key}")


def to_sentence(name):
    title = name.replace('-', ' ')
    title = title.replace('ccw', 'CCW')
    title = title.replace('cw', 'CW')
    title = title[0].upper() + title[1:]
    return title


def generate_script(name, mod, key):
    try:
        title = to_sentence(name)
        mods = mods_csv(mod)
        command = key_cmd(key)
        script = script_template.replace('<<title>>', title).replace('<<command>>', command).replace('<<mods>>', mods)
        
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        filepath = os.path.join(__location__, f"{name}.applescript")
        with open(filepath, 'w') as f:
            f.write(script)
    except ValueError:
        print(f"Unable to generate script for key (name: {name}, mod: {mod}, key: {key})")


def generate_scripts(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict) and value.get('key') is not None and value.get('mod') is not None:
                print(f"Generating script for {key}")
                generate_script(key, value['mod'], value['key'])


def parse_config_file(file_path):
    try:
        with open(file_path, "r") as f:
            config_data = yaml.safe_load(f)  
            # If the config file is empty exit.
            if config_data is None:
                print("The configuration file is empty or incorrectly formatted.")
                exit(3)
            return config_data

    except FileNotFoundError:
        print(f"Error: Config file not found at {file_path}.")
        exit(1)

    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        exit(2)


def main():
    # Parse the configuration file.
    config_data = parse_config_file(config_file_path) 
    
    # Generate scripts based on the parsed YAML data.
    generate_scripts(config_data) 

if __name__ == "__main__":
    main()
