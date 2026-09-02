# Viking home matches calendar

This repository creates a read-only calendar feed containing upcoming Viking home matches. GitHub Actions downloads the public Viking calendar once per day, filters it, and publishes the result through GitHub Pages.

## Subscribe

After GitHub Pages has been enabled, subscribe to this URL in Apple Calendar, Google Calendar, Outlook, or another iCalendar-compatible application:

```text
https://OWNER.github.io/REPOSITORY/viking_home_matches.ics
```

Replace `OWNER` and `REPOSITORY` with the GitHub account and repository name. Use the calendar application's **subscribe** or **add calendar from URL** option, not its one-time import option.

## Setup

1. Make this repository public. Calendar applications must be able to access the published feed without GitHub authentication.
2. In the repository, open **Settings > Pages** and set the source to **GitHub Actions**.
3. Open **Actions > Publish calendar feed**, choose **Run workflow**, and run it once.
4. Subscribe using the URL above.

The scheduled workflow runs daily at approximately 05:17 UTC. GitHub may delay scheduled workflows, so the update time is not exact. You can run it manually whenever an immediate refresh is needed.

## Filtering rules

- The event summary must begin with `Viking - `, matching the original script.
- Only events whose start time has not passed are included.
- Events with `STATUS:CANCELLED` or `STATUS:POSTPONED` are excluded.
- Calendar metadata, time zones, event properties, and UIDs are preserved so calendar applications can recognize updates.

## Manual testing

From the repository directory, install the dependency, download the source feed, and generate a local output file:

```bash
python3 -m pip install -r requirements.txt
curl --fail --location --retry 3 -o full.ics "https://www.vikingfotball.no/terminliste/subscribe"
python3 filter_ics.py full.ics viking_home_matches.ics
```

Check that the output exists and contains a valid calendar:

```bash
grep -c "BEGIN:VEVENT" viking_home_matches.ics
grep "SUMMARY:" viking_home_matches.ics
grep "STATUS:" viking_home_matches.ics
```

You should see only upcoming summaries beginning with `Viking - `, with no cancelled or postponed events. Open `viking_home_matches.ics` in a text editor to inspect the event dates and UIDs. You can import this file for a one-time check, but use the GitHub Pages URL for automatic updates.

To test the GitHub workflow, push these files to GitHub, enable Pages, then use **Actions > Publish calendar feed > Run workflow**. The published feed will be available at:

```text
https://OWNER.github.io/REPOSITORY/viking_home_matches.ics
```

## Troubleshooting

If the feed is empty or a match is missing, check the source event's `SUMMARY`, `DTSTART`, and `STATUS` values. View the latest workflow run under **Actions** for download or parsing errors.