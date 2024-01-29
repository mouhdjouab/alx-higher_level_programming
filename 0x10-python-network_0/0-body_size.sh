#!/bin/bash
# Get the byte size for  URL.
curl -s "$1" | wc -c
