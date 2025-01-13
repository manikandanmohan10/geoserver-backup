#!/bin/bash

MAIN_PATH="/home/ss-pr-cpu-37nwe/cproject/strategy/code/docker-geoserver/geoserver-backup/"
echo "Into the container..."

docker exec -t kartozageoserver-db-1 bash -c "
    echo 'Creating .pgjson file ..'
    cd /root
    echo \"localhost:5432:*:docker:docker\" > ~/.pgpass
    chmod 0600 ~/.pgpass
    exit
"

echo 'Give permission ..'

chmod +x "$MAIN_PATH"start_backup.sh

echo 'Create crontab .'

# Directly add the cron job without opening the editor
echo "0 3 * * * $MAIN_PATH"script.sh" | crontab -

cd "$MAIN_PATH"
bash start_backup.sh
