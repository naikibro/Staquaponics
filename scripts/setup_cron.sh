#!/bin/bash

# Flags for determining which commands to add
add_client_commands=false
add_server_command=false

# Parse command-line arguments for flags
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -client) add_client_commands=true ;;
        -server) add_server_command=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Reset the crontab
crontab -r

# Define environment variable for cron context
envVar="USER=$USER"
echo "$envVar" | crontab -

# Define the commands
command1="*/15 6-18 * * * /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/take_photo.py"
command2="59 17 * * * /bin/bash /home/$USER/Desktop/Staquaponics/scripts/sync.sh"
command3="@reboot cd /home/$USER/Desktop/Staquaponics/staquaponics/ && nohup npm run dev &"

# Check flags and add commands to crontab as necessary
{
    echo "$envVar" # Ensure the environment variable is always set
    if [ "$add_client_commands" = true ]; then
        echo "$command1"
        echo "$command2"
    fi
    if [ "$add_server_command" = true ]; then
        echo "$command3"
    fi
} | crontab -

echo "Crontab updated successfully."
