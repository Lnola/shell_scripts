#!/bin/bash

osascript<<EOF
    tell application "$1" to activate
    do shell script "amethyst/throw-space-n.sh $2"
EOF
