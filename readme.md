Before running script note:

- Replace 'service_account.json' with the path to your service account key file.
- Replace 'your_folder_id_here' with your Google Drive folder ID or leave it None for the root folder.
- Replace 'backup_folder' with the path to the directory you want to back up.

To setup corn for script:

1. Edit the Crontab File:

```
crontab -e
```

2. Add a New Cron Job:
Suppose you want to run the script every day at 2:00 AM:

```
0 2 * * * /usr/bin/python3 /path/to/drive_backup.py
```

Explanation:

```
Minute  Hour  Day  Month  Day_of_Week  Command
0       2     *    *      *            /usr/bin/python3 /path/to/drive_backup.py
```

3. Save and Exit:

Press `CTRL + X → Y → Enter`.

4. Verify Scheduled Jobs:

```
crontab -l
```

5. Check Logs (Optional):

```
grep CRON /var/log/syslog
```
