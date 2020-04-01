#!/bin/bash

# sh black.sh

BLUE="\033[1;34m" # Light blue
NOCOLOR="\033[0m"

# In order to exclude the `build` folder, add `-path ./build -prune -o`
find . -path ./build -prune -o -name "*.py" \
    -exec printf "\n ${BLUE}"{}"${NOCOLOR}\n" \; \
    -exec black --target-version py37 {} \; \
    -exec printf "\n" \;
