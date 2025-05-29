#!/bin/bash

location="$1"
if [ -z "$location" ]; then
    echo "Missing argument location of the root folder"
    exit 1
fi
cp -r $location/hooks $location/.git
chmod +x $location/.git/hooks/*
