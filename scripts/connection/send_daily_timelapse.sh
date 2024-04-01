#!/bin/bash

# Load environment variables from .env file
if [[ -f .env ]]; then
    source .env
else
    echo "Environment file .env not found."
    exit 1
fi

# Check if destination folder exists on the remote server, if not, create it
ssh "$USER@$VIDEO_SERVER_URL" "mkdir -p $WEBSERVER_VIDEOS_FOLDER"

# Upload the contents of the local VIDEOS_FOLDER directory to the remote VIDEOS_FOLDER directory
scp -r "$VIDEOS_FOLDER/" "$USER@$VIDEO_SERVER_URL:$WEBSERVER_VIDEOS_FOLDER/../"

# Append the filename with filetype to videos.json on the remote server
for file in $VIDEOS_FOLDER/*; do
    filename=$(basename "$file")
    filetype="${filename##*.}"
    # Construct JSON snippet
    json_snippet="{\"name\":\"$filename\",\"type\":\"$filetype\"}"
    # Append JSON snippet to videos.json on remote server
    ssh "$USER@$VIDEO_SERVER_URL" "echo $json_snippet >> $WEBSERVER_VIDEOS_FOLDER/../videos.json"
done