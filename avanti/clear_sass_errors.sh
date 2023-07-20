#!/bin/bash

# Check if folder path and file extension are provided as arguments
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <folder_path> <file_extension>"
  exit 1
fi

# Store the folder path and file extension in variables
folder_path="$1"
file_extension="$2"

# Step 1: Remove any mention of "@use "sass:math""
# Step 2: Replace all occurrences of "math.div(x, y)" with "calc(x / y)"
# Apply the changes to files with the specified extension in the selected folder and its subdirectories
find "$folder_path" -type f -name "*.$file_extension" -exec sed -E -i '' \
  -e '/@use "sass:math"/d' \
  -e 's/math\.div\(([^)]*), ([^)]*)\)/calc(\1 \/ \2)/g' \
  {} \;

echo "Conversion complete. Contents of files with extension .$file_extension in folder $folder_path have been updated."
