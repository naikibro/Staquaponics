import os
from dotenv import load_dotenv
import subprocess
from environment import EnvironmentVariables

def compile_images_to_video(images_folder, videos_folder, system_name):
    # Ensure the output directory exists
    os.makedirs(videos_folder, exist_ok=True)

    # Create video filename based on system name and current timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    video_filename = f"{timestamp}-{system_name}-timelapse.mp4"
    video_path = os.path.join(videos_folder, video_filename)

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

def main():
    # Load environment variables
    env = EnvironmentVariables()

    # Compile images to video
    compile_images_to_video(env.IMAGES_FOLDER, env.VIDEOS_FOLDER, env.SYSTEM_NAME)

if __name__ == "__main__":
    main()
