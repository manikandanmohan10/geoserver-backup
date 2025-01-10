#!/bin/bash

# Variables
CONTAINER_NAME="kartozageoserver-db-1"
BACKUP_DIR="/backup"
DATE_DIR=$(date +%Y-%m-%d)
POSTGRES_USER="postgres"
HOST="localhost"
GIS_DB="gis"
GWC_DB="gwc"

# Enter Docker container
docker exec -it $CONTAINER_NAME bash -c "
    # Check and create backup directory if it doesn't exist
    if [ ! -d \"$BACKUP_DIR\" ]; then
        mkdir $BACKUP_DIR
    fi
    
    # Navigate to backup directory
    cd $BACKUP_DIR
    
    # Create folder with current date
    mkdir -p $DATE_DIR
    
    # Perform backups
    pg_dump -U $POSTGRES_USER -h $HOST -F c -b -v -f $BACKUP_DIR/$DATE_DIR/gis.backup $GIS_DB
    pg_dump -U $POSTGRES_USER -h $HOST -F c -b -v -f $BACKUP_DIR/$DATE_DIR/gwc.backup $GWC_DB
"
