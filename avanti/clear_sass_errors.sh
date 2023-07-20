#!/bin/bash

# Check if a filename is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

# Store the filename in a variable
filename="$1"

# Step 1: Remove any mention of "@use "sass:math""
# Step 2: Replace all occurrences of "math.div(x, y)" with "calc(x / y)"
# Save the changes to a temporary file
sed -E \
  -e '/@use "sass:math"/d' \
  -e 's/math\.div\(([^)]*), ([^)]*)\)/calc(\1 \/ \2)/g' \
  "$filename" > "${filename}.temp"

# Move the temporary file back to the original filename
mv "${filename}.temp" "$filename"

echo "Conversion complete. Contents of $filename have been updated."
