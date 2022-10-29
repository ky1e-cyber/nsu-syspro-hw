#!/bin/sh

FILES="${@:2}"
VERBOSE=false
SUFFIX="$1"


if [ "$1" = "-v" ]; then
  FILES="${@:3}"
  VERBOSE=true
  SUFFIX="$2"
fi

for file_name in "$FILES"; do

  if [ "$VERBOSE" = true ]; then
    echo "renaming $file_name to $file_name$SUFFIX"
  fi

  mv "$file_name" "$file_name$SUFFIX"

done

