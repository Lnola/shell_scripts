#!/bin/bash

# Path to the previously created script
COPY_SCRIPT_PATH="$HOME/bin/scripts/copy-file-to-location.sh"

# Check if the .env file path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_env_file>"
    exit 1
fi

ENV_FILE="$1"

# Check if the .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "The .env file does not exist."
    exit 2
fi

# Read each line from the .env file
while IFS='=' read -r src dst; do
    # Check if src and dst are not empty
    if [[ -n "$src" && -n "$dst" ]]; then
        echo "Copying $src to $dst..."
        # Call the copy script with source file and destination directory
        "$COPY_SCRIPT_PATH" "$src" "$dst"
    fi
done < "$ENV_FILE"
