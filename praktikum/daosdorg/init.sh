#!/bin/bash

# Compare the flag in main.c and challenge.yml
flag_main=$(grep -oE 'Orkom\{[^}]+\}' src/main.c)
flag_yml=$(grep -oE 'Orkom\{[^}]+\}' challenge.yml)
if [[ "$flag_main" != "$flag_yml" ]]; then
    echo "Flags do not match!"
    echo "$flag_main"
    echo "$flag_yml"
    exit 1
fi

# Compile the main.c and client.c file
cp src/main.c src/client.c
sed -i -E 's/Orkom\{[^}]*\}/Orkom{XXXXXXXXXXXXXXXX}/g' src/client.c
make build

# Create a docker compose instance
docker compose up --build -d --force-recreate

# Copy to the writeup folder & initialize
cp dist/client writeup/client
cd writeup && pwninit
