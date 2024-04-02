#!/bin/bash

# Loop 10 times
for i in {1..100}
do
    /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/take_photo.py
done

/usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/compile_day.py
/bin/bash /home/$USER/Desktop/Staquaponics/scripts/connection/send_daily_timelapse.sh
/bin/bash /home/$USER/Desktop/Staquaponics/scripts/flush_daily_data.sh