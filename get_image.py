#!/usr/bin/env python3
"""
M5UnitV2 Camera Image Fetcher for Raspberry Pi
Fetches images from the M5UnitV2 camera over Ethernet-over-USB.
Starts the camera's Flask server if it's not running.
=== USAGE ===
1. Save as `/home/sarahbot/get_image.py`.
2. Make executable: `chmod +x /home/sarahbot/get_image.py`.
3. Run: `python3 /home/sarahbot/get_image.py`.
=== NOTES ===
- Requires passwordless SSH to the camera.
- Camera must have `imageserver.py` in `/home/m5stack/imageserver/`.
- Image saved to `/home/sarahbot/2026/latest.jpg`.
"""
import requests
import subprocess
import time

CAMERA_IP = "10.254.239.1"
CAMERA_USER = "m5stack"
SERVER_SCRIPT = "/home/m5stack/imageserver/imageserver.py"
IMAGE_URL = f"http://{CAMERA_IP}:5000/snapshot"
IMAGE_PATH = "/home/sarahbot/2026/latest.jpg"

def is_server_running():
    """Check if the camera's Flask server is running."""
    try:
        response = requests.get(IMAGE_URL, timeout=5)
        return response.status_code == 200
    except:
        return False

def start_server():
    """Start the camera's Flask server via SSH."""
    print("Starting camera server...")
    cmd = f'ssh -f {CAMERA_USER}@{CAMERA_IP} "sudo chmod 666 /dev/video0 && nohup /usr/bin/python3 {SERVER_SCRIPT} &"'
    subprocess.run(cmd, shell=True, check=True)
    time.sleep(3)  # Give the server time to start

def fetch_image():
    """Fetch the latest image from the camera."""
    try:
        response = requests.get(IMAGE_URL, timeout=10)
        if response.status_code == 200:
            with open(IMAGE_PATH, "wb") as f:
                f.write(response.content)
            print(f"Image saved to {IMAGE_PATH}")
        else:
            print(f"Server error: {response.status_code}")
    except Exception as e:
        print(f"Failed to fetch image: {e}")

def main():
    if not is_server_running():
        start_server()
    fetch_image()

if __name__ == "__main__":
    main()
