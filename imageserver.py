#!/usr/bin/env python3
"""
Flask server for M5UnitV2 camera.
Serves a snapshot on demand at /snapshot.
=== USAGE ===
1. Save as `/home/m5stack/imageserver/imageserver.py`.
2. Make executable: `chmod +x /home/m5stack/imageserver/imageserver.py`.
3. Run: `python3 /home/m5stack/imageserver/imageserver.py`.
=== NOTES ===
- Requires `fswebcam` for capturing images.
- Runs on port 5000.
"""
from flask import Flask, Response
import subprocess
import time

app = Flask(__name__)

def capture_image():
    """Capture an image using fswebcam."""
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", "/tmp/snapshot.jpg"])
    with open("/tmp/snapshot.jpg", "rb") as f:
        return f.read()

@app.route('/snapshot')
def snapshot():
    """Serve the latest snapshot."""
    return Response(capture_image(), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
