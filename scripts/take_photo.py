import cv2
import os
from datetime import datetime
import logging
from environment import EnvironmentVariables

def take_photo(IMAGES_FOLDER, SYSTEM_NAME, CAMERA_ADDRESS):

    IMAGES_FOLDER = os.path.expandvars(IMAGES_FOLDER)

    # Configure logging
    log_file = '/home/naiki/Desktop/Staquaponics/logs.txt'
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

    # Ensure IMAGES_FOLDER exists
    if not os.path.exists(IMAGES_FOLDER):
        os.makedirs(IMAGES_FOLDER)

    # Initialize camera
    # Assuming CAMERA_ADDRESS is the index; converting to integer
    camera = cv2.VideoCapture(int(CAMERA_ADDRESS))

    # Check if camera opened successfully
    if not camera.isOpened():
        logging.error("Error: Could not open camera")
        exit()

    # Capture a frame
    ret, frame = camera.read()

    # Check if frame is captured
    if not ret:
        logging.error("Error: Could not read frame")
        exit()

    # Generate filename
    current_time = datetime.now().strftime('%Y-%m-%d-%H-%M')
    filename_base = f"{current_time}-{SYSTEM_NAME}-image"
    filepath = os.path.join(IMAGES_FOLDER, filename_base + ".jpg")
    print(filepath)

    # Check if filename already exists, if yes, append a number
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(IMAGES_FOLDER, f"{filename_base}-{counter}.jpg")
        counter += 1

    # Save image
    cv2.imwrite(filepath, frame)

    # Release the camera
    camera.release()

    logging.info(f"Image saved to {filepath}")

def main():
    # Load environment variables
    env = EnvironmentVariables()

    # Compile images to video
    take_photo(env.IMAGES_FOLDER, env.SYSTEM_NAME, env.CAMERA_ADDRESS)

if __name__ == "__main__":
    main()
