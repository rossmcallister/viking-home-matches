#!/usr/bin/env bash

set -euo pipefail

INPUT="${1:-full.ics}"
OUTPUT="${2:-viking_home_matches.ics}"

if [[ ! -f "$INPUT" ]]; then
    echo "ERROR: $INPUT not found." >&2
    exit 1
fi

python3 filter_ics.py "$INPUT" "$OUTPUT"
echo "Created: $OUTPUT"