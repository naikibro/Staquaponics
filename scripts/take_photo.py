# take_photo.py
import cv2
import os
from datetime import datetime
from environment import EnvironmentVariables

# Environment variables
env_vars = EnvironmentVariables()

# Ensure IMAGES_FOLDER exists
if not os.path.exists(env_vars.IMAGES_FOLDER):
    os.makedirs(env_vars.IMAGES_FOLDER)

# Initialize camera
# Assuming CAMERA_ADDRESS is the index; converting to integer
camera = cv2.VideoCapture(int(env_vars.CAMERA_ADDRESS))

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
filename_base = f"{current_time}-{env_vars.SYSTEM_NAME}-image"
filepath = os.path.join(env_vars.IMAGES_FOLDER, filename_base + ".jpg")

# Check if filename already exists, if yes, append a number
counter = 1
while os.path.exists(filepath):
    filepath = os.path.join(env_vars.IMAGES_FOLDER, f"{filename_base}-{counter}.jpg")
    counter += 1

# Save image
cv2.imwrite(filepath, frame)

# Release the camera
camera.release()

print(f"Image saved to {filepath}")
