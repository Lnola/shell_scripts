#!/bin/bash

# Path to the previously created script
COPY_SCRIPT_PATH="$HOME/bin/scripts/copy-file-to-location.sh"

# Check if the JSON file path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_json_file>"
    exit 1
fi

JSON_FILE="$1"
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
    fi
done
