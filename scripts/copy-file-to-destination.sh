#!/bin/bash

# Initialize variables
with_check=false
source_file=""
destination_file=""

SCRIPT_DIR=$(dirname "$(realpath "$BASH_SOURCE")")

# Parse arguments to handle --with-check flag and file paths
for arg in "$@"; do
    if [[ "$arg" == "--with-check" ]]; then
        with_check=true
    elif [[ -z "$source_file" ]]; then
        source_file=$arg
    else
        destination_file=$arg
    fi
done

# Verify that source_file and destination_file are provided
if [[ -z "$source_file" || -z "$destination_file" ]]; then
    echo "Usage: $0 <source_file> <destination_file> [--with-check]"
    exit 1
fi

# Function to ask user for overwrite confirmation
ask_overwrite_confirmation() {
    read -p "Do you want to overwrite it? (yes/no): " user_choice
    user_choice_lower=$(echo "$user_choice" | tr '[:upper:]' '[:lower:]')
    
    if [[ "$user_choice_lower" == "yes" || "$user_choice_lower" == "y" ]]; then
        return 0 # User confirms overwrite
    else
        return 1 # User cancels overwrite
    fi
}

# Check if the check-file-diff.sh script should be run
if $with_check && [ -e "$destination_file" ]; then
    # Path to the check-file-diff.sh script
    CHECK_SCRIPT_PATH="$SCRIPT_DIR/check-file-diff.sh"

    # Call the check script and pass necessary arguments
    "$CHECK_SCRIPT_PATH" "$source_file" "$destination_file"
    check_result=$?

    if [ $check_result -eq 1 ]; then
        # The check script found differences or the file exists, ask user for confirmation
        ask_overwrite_confirmation "$destination_file"
        if [ $? -ne 0 ]; then
            echo "Operation cancelled by the user."
            exit 2
        fi
    fi
fi

# If the change is not requested
cp "$source_file" "$destination_file"
if [ $? -ne 0 ]; then
    echo "Failed to copy the file."
    exit 3
fi
echo "File copied successfully."
