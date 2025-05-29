#!/bin/bash

# TODO: Rewrite in python to passing list of staged files to the script
# that way the apply is called only for the truly changed files
# Path to the previously created script
COPY_SCRIPT_PATH="$HOME/bin/scripts/copy-file-to-destination.sh"

# Determine the script's directory
SCRIPT_DIR=$(dirname "$(realpath "$BASH_SOURCE")")

# Default JSON file path, relative to the script's location
DEFAULT_JSON_FILE="$SCRIPT_DIR/.config.json"

# Check if the JSON file path is provided
if [ "$#" -ne 1 ]; then
    echo "No path provided. Using default JSON file path: $DEFAULT_JSON_FILE"
    echo
    JSON_FILE="$DEFAULT_JSON_FILE"
else
    JSON_FILE="$1"
fi

# Determine the directory of the JSON file
JSON_FILE_DIR=$(dirname "$(realpath "$JSON_FILE")")

# Check if the JSON file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "The JSON file does not exist."
    exit 2
fi

# Process each source and destination from the JSON file
length=$(jq '. | length' "$JSON_FILE")
for ((i = 0 ; i < length ; i++)); do
    src=$(jq -r ".[$i].source" "$JSON_FILE")
    dst=$(jq -r ".[$i].destination" "$JSON_FILE")
    
    # Resolve full paths
    src_abs="$JSON_FILE_DIR/$src"
    dst_abs="$JSON_FILE_DIR/$dst"
    
    if [[ -n "$src" && -n "$dst" ]]; then
        echo "Copying $src_abs to $dst_abs..."
        # Call the copy script with absolute source and destination paths
        "$COPY_SCRIPT_PATH" "$src_abs" "$dst_abs"
        # Check if the copy operation failed
        if [ $? -ne 0 ]; then
            echo "Failed to copy $src_abs to $dst_abs"
            exit 1
        fi
    fi
done

# If the script reaches this point, all operations were successful
exit 0
