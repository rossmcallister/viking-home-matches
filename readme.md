1. Download the full.ics using this bash command.
curl -k -L "https://www.vikingfotball.no/terminliste/subscribe" -o full.ics

2. Install prerequisites: - macOS/Linux: Already installed (bash, curl). - Windows: Install Git (includes Git Bash) or enable WSL.

3. Create the script file: - Open a text editor (Notepad, VS Code, nano, etc.).

4. Save file as viking_home_ics.sh
Copy the script content: - Paste the full script into the file. - Save and close the file.

5. Open terminal: - macOS: Terminal app. - Linux: Terminal. - Windows: Git Bash or WSL.

6. Navigate to script folder: - Use: cd path/to/your/script

7. Make script executable (macOS/Linux): - chmod +x viking_home_ics.sh

8. Run the script: - ./viking_home_ics.sh OR - bash viking_home_ics.sh

9. Verify output: - A file named viking_home_matches.ics should be created.

10. Import into calendar: - Open Outlook, Google Calendar, or Apple Calendar. - Import the .ics file.

11. Optional automation: - Set up cron (macOS/Linux) or Task Scheduler (Windows) to run periodically