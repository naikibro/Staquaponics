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

# Download the current videos.json or initialize it as an empty list
if ssh "$USER@$VIDEO_SERVER_URL" "[ -f '$WEBSERVER_VIDEOS_FOLDER/videos.json' ]"; then
    scp "$USER@$VIDEO_SERVER_URL:$WEBSERVER_VIDEOS_FOLDER/videos.json" /tmp/videos.json
else
    echo "[]" > /tmp/videos.json
fi

# Use a temporary file to store the new JSON array
temp_file=$(mktemp)

# Initialize the JSON array string
json_array="["

# Fetch the list of files in the remote video folder, loop through them
while IFS= read -r file; do
    filename=$(basename "$file")
    filetype="${filename##*.}"
    # Append the JSON object to the array string, add a comma after every entry
    json_array+="{\"name\":\"$filename\",\"type\":\"$filetype\"},"
done < <(ssh "$USER@$VIDEO_SERVER_URL" "find '$WEBSERVER_VIDEOS_FOLDER' -type f -printf '%f\n'")

# Remove the last comma to maintain valid JSON syntax
json_array="${json_array%,}"

# Close the JSON array
json_array+="]"

# Save the JSON array to the temporary file
echo "$json_array" > "$temp_file"

# Move the updated file back to /tmp/videos.json
mv "$temp_file" /tmp/videos.json

# Upload the modified videos.json back to the remote server
scp /tmp/videos.json "$USER@$VIDEO_SERVER_URL:$WEBSERVER_VIDEOS_FOLDER/videos.json"

# Clean up local temporary files
rm /tmp/videos.json*
