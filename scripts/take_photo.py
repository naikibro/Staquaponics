# take_photo.py

"""
env variables:
- CAMERA_ADRESS
- IMAGES_FOLDER
- SYSTEM_NAME

this script takes a picture using opencv on the CAMERA_ADRESS and sotres it in IMAGES_FOLDER

filetype example( 1080 * 720 ): 
    YYYY-MM-DD-HH-MM-SYSTEM_NAME-image.jpg
"""

import cv2
import os
from datetime import datetime

# Environment variables
CAMERA_ADDRESS = os.getenv('CAMERA_ADRESS', '0')  # Default to 0 if not set
IMAGES_FOLDER = os.getenv('IMAGES_FOLDER', './images')
SYSTEM_NAME = os.getenv('SYSTEM_NAME', 'STAQUAPONICS')

# Ensure IMAGES_FOLDER exists
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

# Initialize camera
# Assuming CAMERA_ADDRESS is the index; converting to integer
camera = cv2.VideoCapture(int(CAMERA_ADDRESS))

# Check if camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera")
    exit()

# Capture a frame
ret, frame = camera.read()

# Check if frame is captured
if not ret:
    print("Error: Could not read frame")
    exit()

# Generate filename
current_time = datetime.now().strftime('%Y-%m-%d-%H-%M')
filename = f"{current_time}-{SYSTEM_NAME}-image.jpg"
filepath = os.path.join(IMAGES_FOLDER, filename)

# Save image
cv2.imwrite(filepath, frame)

# Release the camera
camera.release()

print(f"Image saved to {filepath}")
