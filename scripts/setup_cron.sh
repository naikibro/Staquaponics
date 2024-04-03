#!/bin/bash

# Reset the crontab
crontab -r

# Define env variables for cron context
envVar1="USER=$USER"
echo "$envVar1" | crontab -

# Define the commands to be added to crontab
command1="*/15 6-17 * * * /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/take_photo.py"
command2="59 17 * * * /bin/bash /home/$USER/Desktop/Staquaponics/scripts/sync.sh"
#command3="@reboot cd /home/$(whoami)/Desktop/Staquaponics/staquaponics/ && npm run dev"

# Add commands to crontab
(crontab -l ; echo "$command1") | crontab -
(crontab -l ; echo "$command2") | crontab -
#(crontab -l ; echo "$command3") | crontab -
