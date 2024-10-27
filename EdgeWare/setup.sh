#!/bin/bash

version_string=$(python3 --version)
if [ $? -ne 0 ]; then
    echo "Python not found"
    exit
fi

IFS=" " read -r p version <<< "$version_string"
IFS="." read -r major minor patch <<< "$version"
if (( !($major == 3 && $minor >= 12) )); then
    echo "Python version 3.12 or higher required"
fi

python3 -m venv venv
if [ $? -eq 0 ]; then
    source venv/bin/activate
else
    echo "Failed to create virtual environment"
    exit
fi

python3 start.pyw