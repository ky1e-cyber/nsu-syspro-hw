#!/bin/sh

for i in {1..100}; do

  TOPRINT=""
  FLAG=false

  if [ "$((i % 3))" = 0 ]; then
    FLAG=true
    TOPRINT+="Fizz"  
  fi

  if [ "$((i % 5))" = 0 ]; then
    FLAG=true
    TOPRINT+="Buzz"
  fi

  if [ "$FLAG" = false ]; then
    TOPRINT="$i"
  fi

  echo "$TOPRINT"

done
