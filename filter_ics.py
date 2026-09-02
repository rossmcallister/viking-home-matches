#!/usr/bin/env python3
"""Create a subscribable ICS feed containing upcoming Viking home matches."""

import argparse
import datetime as dt
from pathlib import Path

from icalendar import Calendar


SUMMARY_PREFIX = "Viking - "
EXCLUDED_STATUSES = {"CANCELLED", "POSTPONED"}


def _start_instant(component):
    value = component.decoded("DTSTART")
    if isinstance(value, dt.datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=dt.timezone.utc)
        return value.astimezone(dt.timezone.utc)
    return dt.datetime.combine(value, dt.time.min, tzinfo=dt.timezone.utc)


def filter_calendar(source, now=None):
    """Return a parsed calendar containing only eligible upcoming events."""
    calendar = Calendar.from_ical(source)
    if calendar.get("VERSION") is None:
        raise ValueError("source is not an iCalendar file")

    now = now or dt.datetime.now(dt.timezone.utc)
    result = Calendar()
    for key, value in calendar.items():
        result.add(key, value)

    for event in calendar.walk("VEVENT"):
        summary = str(event.get("SUMMARY", ""))
        status = str(event.get("STATUS", "")).upper()
        if (
            summary.startswith(SUMMARY_PREFIX)
            and status not in EXCLUDED_STATUSES
            and _start_instant(event) >= now
        ):
            result.add_component(event)
    return result


def convert_file(source_path, output_path, now=None):
    source = Path(source_path).read_bytes()
    if b"BEGIN:VCALENDAR" not in source:
        raise ValueError("source is not an iCalendar file")
    output = filter_calendar(source, now=now).to_ical()
    destination = Path(output_path)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_bytes(output)
    temporary.replace(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="path to the source ICS file")
    parser.add_argument("destination", help="path for the filtered ICS file")
    args = parser.parse_args()
    convert_file(args.source, args.destination)


if __name__ == "__main__":
    main()