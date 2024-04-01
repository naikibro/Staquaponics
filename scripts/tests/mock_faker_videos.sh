#!/bin/bash

for i in {1..10}
do
    /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/take_photo.py
done

for i in {1..3}
do
    /usr/bin/python3 /home/$USER/Desktop/Staquaponics/scripts/compile_day.py
done


