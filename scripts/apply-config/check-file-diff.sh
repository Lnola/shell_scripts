#!/bin/bash

# This script checks for file existence at the destination and shows diff
source_file="$1"
destination_file="$2"

filename=$(basename "$source_file")

# Check if the file exists in the destination directory
if [ -e "$destination_file" ]; then
    echo "File $filename already exists at destination. Showing differences:"
    code -d "$destination_file/$filename" "$source_file"
    exit 1
else
    echo "File does not exist at the destination, okay to copy"
    exit 0
fi
