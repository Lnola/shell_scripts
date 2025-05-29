#!/bin/bash

# Check the current working directory matches the location
location="/Projects/solution-tree-platform"
if [ "$(pwd)" != "$HOME$location" ]; then
    echo "Error: Script must be run from the ~$location folder."
    exit 1
fi

# Execute the command and capture the output in a variable
services_list_output=$(brew services list)
test_db_name="postgresql@14 started"
# Check if the test db is active
if [[ "$services_list_output" == *$test_db_name* ]]; then
    read -p "Warning: You are working with the *TEST* database. Do you wish to proceed? (Y/N): " response
    if [ "$response" == "N" ] || [ "$response" == "n" ]; then
        exit 0
    fi
fi

npm run db:migration:up
npm run db:seed
