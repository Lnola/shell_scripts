#!/bin/bash

# Check if exactly 2 arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_file> <destination_directory>"
    exit 1
fi

# Extract filename from the first argument
filename=$(basename "$1")

# Check if the file exists in the destination directory
if [ -e "$2/$filename" ]; then
    # Check if the files are the same
    if cmp -s "$1" "$2/$filename"; then
        echo "The files are identical. No action required."
    else
        echo "File $filename already exists at destination. Showing differences:"
        # Show differences
        code -d "$2/$filename" "$1"
        
        # Ask the user for input
        read -p "Do you want to overwrite the file? (yes/no): " user_choice
        user_choice_lower=$(echo "$user_choice" | tr '[:upper:]' '[:lower:]')
        
        if [ "$user_choice_lower" = "yes" ] || [ "$user_choice_lower" = "y" ]; then
            # If the user wants to overwrite, copy the file
            cp "$1" "$2"
            echo "File has been overwritten."
        else
            echo "Operation cancelled by the user."
            exit 2
        fi
    fi
else
    # If the file does not exist, directly copy the file
    cp "$1" "$2"
    if [ $? -ne 0 ]; then
        echo "Failed to copy the file."
        exit 3
    fi
    echo "File copied successfully."
fi
