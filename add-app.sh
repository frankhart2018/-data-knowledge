#!/bin/bash

if [ -z $1 ]; then
    echo "Usage: $0 <app-name>"
    exit 1
fi

mkdir apps/pages/$1
mkdir apps/pages/$1/pages
mkdir apps/pages/$1/data
touch apps/pages/$1/main.py