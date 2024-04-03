import os
from dotenv import load_dotenv

class EnvironmentVariables:
    def __init__(self, env_file="../.env"):
        self.env_file = os.path.join(os.path.dirname(__file__), env_file)
        self.load_env_variables()

    def load_env_variables(self):
        load_dotenv(self.env_file)

        # Accessing environment variables
        self.SYSTEM_NAME = os.getenv("SYSTEM_NAME")
        self.CAMERA_ADDRESS = os.getenv("CAMERA_ADDRESS")
        self.CAMERA_TYPE = os.getenv("CAMERA_TYPE")
        self.NUMBER_OF_CAMERAS = str(os.getenv("NUMBER_OF_CAMERAS"))
        self.NUMBER_OF_DEVICES = str(os.getenv("NUMBER_OF_DEVICES"))
        self.IMAGES_FOLDER = os.getenv("IMAGES_FOLDER")
        self.VIDEOS_FOLDER = os.getenv("VIDEOS_FOLDER")
        self.SIZE_HANDLING_LOG = os.getenv("SIZE_HANDLING_LOG")
        self.LOCAL_NETWORK = os.getenv("LOCAL_NETWORK")
        self.VIDEO_SERVER_URL = os.getenv("VIDEO_SERVER_URL")
        self.CLOUDFLARE_TUNNEL_TOKEN = os.getenv("CLOUDFLARE_TUNNEL_TOKEN")

        # Expand environment variables and tilde character for paths
        self.IMAGES_FOLDER = os.path.expandvars(os.path.expanduser(self.IMAGES_FOLDER))
        self.VIDEOS_FOLDER = os.path.expandvars(os.path.expanduser(self.VIDEOS_FOLDER))
        self.SIZE_HANDLING_LOG = os.path.expandvars(os.path.expanduser(self.SIZE_HANDLING_LOG))

    def print_env_variables(self):
        # Print variables loaded from .env file
        print("\n---------------\n")
        print("\nVariables from .env file:")
        print("\tSYSTEM_NAME:", self.SYSTEM_NAME)
        print("\tCAMERA_ADDRESS:", self.CAMERA_ADDRESS)
        print("\tCAMERA_TYPE:", self.CAMERA_TYPE)
        print("\tNUMBER_OF_CAMERAS:", self.NUMBER_OF_CAMERAS)
        print("\tNUMBER_OF_DEVICES:", self.NUMBER_OF_DEVICES)
        print("\tIMAGES_FOLDER:", self.IMAGES_FOLDER)
        print("\tVIDEOS_FOLDER:", self.VIDEOS_FOLDER)
        print("\tSIZE_HANDLING_LOG:", self.SIZE_HANDLING_LOG)
        print("\tLOCAL_NETWORK:", self.LOCAL_NETWORK)
        print("\tVIDEO_SERVER_URL:", self.VIDEO_SERVER_URL)
        print("\tCLOUDFLARE_TUNNEL_TOKEN:", self.CLOUDFLARE_TUNNEL_TOKEN)
        print("\n---------------\n")

