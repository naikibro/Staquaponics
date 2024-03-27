#!/bin/bash

# Define the commands to be added to crontab
command1="*/15 6-17 * * * /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/take_photo.py"
command2="59 17 * * * /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/compile_day.py"
command3="59 17 * * * /bin/bash /home/$USER/Desktop/Staquaponics/scripts/connection/send_daily_timelapse.sh"
command4="59 17 * * * /bin/bash /home/$USER/Desktop/Staquaponics/scripts/flush_daily_data.sh"

# Add commands to crontab
(crontab -l ; echo "$command1") | crontab -
(crontab -l ; echo "$command2") | crontab -
(crontab -l ; echo "$command3") | crontab -
(crontab -l ; echo "$command4") | crontab -
