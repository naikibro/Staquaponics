#!/bin/bash

# Load environment variables from .env file
if [[ -f .env ]]; then
    source .env
else
    echo "Error: Environment file .env not found."
    exit 1
fi

# Function to calculate total file size in a folder
calculate_total_size() {
    local folder="$1"
    if [[ -d "$folder" ]]; then
        local total_size=$(du -sb "$folder" | cut -f1) # Summarize total size of files in bytes
        echo "$total_size"
    else
        echo "Error: Folder $folder does not exist."
        exit 1
    fi
}

# Function to delete files and log total size
delete_and_log() {
    local folder="$1"
    local log_file="$2"
    local total_size

    # Calculate the total size before deleting
    total_size=$(calculate_total_size "$folder")

    # Delete the files in the folder if it exists
    if [[ -d "$folder" ]]; then
        rm -rf "$folder"/*
        # Get timestamp
        timestamp=$(date +"%Y-%m-%d %H:%M:%S")
        # Log the total size released with timestamp
        echo "$timestamp - Total size released: $total_size bytes" >> "$log_file"
    else
        echo "Error: Folder $folder does not exist."
        exit 1
    fi
}

# Delete videos, images, and log total size
delete_and_log "$VIDEOS_FOLDER" "$SIZE_HANDLING_LOG"
delete_and_log "$IMAGES_FOLDER" "$SIZE_HANDLING_LOG"

echo "Flush completed."
