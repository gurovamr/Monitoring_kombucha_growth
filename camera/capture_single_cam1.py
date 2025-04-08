import os
from datetime import datetime
import subprocess

# Save path for test images
save_dir = "/home/gurov/Monitoring_kombucha_growth/data/test"
os.makedirs(save_dir, exist_ok=True)  # Create folder if it doesn't exist

# Generate timestamp
timestamp = datetime.now().strftime("%m-%d_%H-%M")

# Output file path
cam_file = os.path.join(save_dir, f"cam1_{timestamp}.jpg")


result = subprocess.run(
    [
        "libcamera-still",
        "--camera", "1",
        "--autofocus-mode", "auto",             # run autofocus once
        "--autofocus-on-capture", "1",          # explicitly trigger focus before capture
        "--autofocus-range", "normal",          # (optional) normal focus range
        "--timeout", "5000",                    # allow more time for autofocus (5 seconds)
        "-o", cam_file
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)


# Check if image was saved
if os.path.exists(cam_file):
    print(f"✅ Image captured: {cam_file}")
else:
    print("❌ cam1 image not saved.")
    print(result.stderr.decode())
