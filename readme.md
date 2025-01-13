## Setup procedure

**Before running script note:**

- Replace 'service_account.json' with the path to your service account key file.
- Replace 'your_folder_id_here' with your Google Drive folder ID or leave it None for the root folder.
- Replace 'backup_folder' with the path to the directory you want to back up.
- Replace 'main.py' in start_backup.sh with full path.


**Setup procedure for backup**

`docker exec -t kartozageoserver-db-1 bash`

Inside container


`cd /root`

`echo "localhost:5432:*:docker:docker" > ~/.pgpass`

`exit`

`chmod 0600 ~/.pgpass`

**To setup corn for script:**

Give permission

```
chmod +x /home/ss-pr-cpu-37nwe/cproject/strategy/code/docker-geoserver/geoserver-backup/start_backup.sh
```

1. Edit the Crontab File:

```
crontab -e
```

2. Add a New Cron Job:
Suppose you want to run the script every day at 2:00 AM:

```
0 3 * * * /path/to/your/script.sh
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

## Running procedure:

**Manual**

`cd geoserver-backup`

Run bash file to get the backup upload

`bash start_backup.sh`