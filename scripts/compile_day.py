import os
import json
import subprocess
import datetime
from environment import EnvironmentVariables

def compile_images_to_video(images_folder, videos_folder, system_name):
    # Ensure the output directory exists
    os.makedirs(videos_folder, exist_ok=True)

    # Create video filename based on system name and current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    base_video_filename = f"{timestamp}-{system_name}-timelapse.mp4"
    video_path = os.path.join(videos_folder, base_video_filename)

    # Check if the video file already exists
    video_filename = base_video_filename
    counter = 1
    while os.path.exists(video_path):
        video_filename = f"{timestamp}-{system_name}-timelapse-{counter}.mp4"
        video_path = os.path.join(videos_folder, video_filename)
        counter += 1

    # Compile images into video using ffmpeg
    ffmpeg_command = [
        "ffmpeg",
        "-framerate", "8",  # Set frame rate to 8 frames per second
        "-pattern_type", "glob",
        "-i", os.path.join(images_folder, "*.jpg"),  # Assuming images are in JPG format
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        video_path
    ]
    subprocess.run(ffmpeg_command)

    print(f"Video compiled: {video_path}")

    # Log the filename to a JSON file
    log_data = {
        "timestamp": timestamp,
        "system_name": system_name,
        "video_filename": video_filename,
        "video_path": video_path
    }

    # Get the webserver log path from environment variables
    webserver_log_path = os.getenv("WEBSERVER_LOG_PATH")

    # If the webserver log path exists, log the data
    if webserver_log_path:
        # Define the path for the JSON log file
        log_file_path = os.path.join(webserver_log_path, "video_logs.json")

        # If the JSON file already exists, load its contents and update
        if os.path.exists(log_file_path):
            with open(log_file_path, "r") as log_file:
                existing_logs = json.load(log_file)
            existing_logs.append(log_data)
            with open(log_file_path, "w") as log_file:
                json.dump(existing_logs, log_file, indent=4)
        else:
            # If the JSON file does not exist, create a new one
            with open(log_file_path, "w") as log_file:
                json.dump([log_data], log_file, indent=4)
    else:
        print("WEBSERVER_LOG_PATH is not set. Unable to log video data.")

def main():
    # Load environment variables
    env = EnvironmentVariables()

    # Compile images to video
    compile_images_to_video(env.IMAGES_FOLDER, env.VIDEOS_FOLDER, env.SYSTEM_NAME)

if __name__ == "__main__":
    main()
