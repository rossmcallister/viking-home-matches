#!/usr/bin/env bash

INPUT="full.ics"
OUTPUT="viking_home_matches.ics"

# Verify source file exists
if [ ! -f "$INPUT" ]; then
    echo "ERROR: $INPUT not found."
    exit 1
fi

# Verify it looks like a calendar file
if ! grep -q "BEGIN:VCALENDAR" "$INPUT"; then
    echo "ERROR: $INPUT is not a valid ICS file."
    exit 1
fi

{
    echo "BEGIN:VCALENDAR"
    echo "VERSION:2.0"
    echo "PRODID:-//Viking Home Matches Filter//EN"

    awk '
    BEGIN {
        in_event = 0
        keep = 0
        event = ""
    }

    /^BEGIN:VEVENT/ {
        in_event = 1
        keep = 0
        event = $0 "\n"
        next
    }

    /^SUMMARY:Viking - / {
        keep = 1
        event = event $0 "\n"
        next
    }

    /^END:VEVENT/ {
        if (in_event) {
            event = event $0 "\n"

            if (keep) {
                printf "%s", event
            }
        }

        in_event = 0
        event = ""
        next
    }

    {
        if (in_event) {
            event = event $0 "\n"
        }
    }
    ' "$INPUT"

    echo "END:VCALENDAR"

} > "$OUTPUT"

echo "Created: $OUTPUT"