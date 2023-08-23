#!/bin/bash

# Get the directory of the run_script.sh file
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <script_name>"
    exit 1
fi

# Construct the script filename by replacing ":" with "_"
script_name="${1//:/_}"
script_path="${script_dir}/scripts/${script_name}.sh"

# Execute the corresponding script
if [ -f "$script_path" ]; then
    "$script_path"
else
    echo "Script '$script_path' not found."
    exit 1
fi
