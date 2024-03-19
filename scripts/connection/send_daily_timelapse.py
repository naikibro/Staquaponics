# send_daily_timelapse.py

"""
env variables:
- VIDEOS_FOLDER
- VIDEO_SERVER_URL
- SYSTEM_NAME

this script sends the daily compiled video inside the VIDEOS_FOLDER to the VIDEO_SERVER_URL usinf scp

filetype example( 1080 * 720 ): 
    YYYY-MM-DD-HH-MM-SYSTEM_NAME-timelapse.avi


scp command to send file to server:

    scp /path/to/file user@server:/path/to/store/the/file

"""

