# !/bin/bash

# Check the current working directory matches the location
location="/Projects/solution-tree-platform"
if [ "$(pwd)" != "$HOME$location" ]; then
    echo "Error: Script must be run from the ~$location folder."
    exit 1
fi

npm run dev:infrastructure -- -d
