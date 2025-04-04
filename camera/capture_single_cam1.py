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


# Capture image from camera 0
result = subprocess.run(
    ["libcamera-still", "--camera", "1", "-o", cam_file],

    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Check if image was saved
if os.path.exists(cam_file):
    print(f"✅ Image captured: {cam_file}")
else:
    print("❌ cam0 image not saved.")
    print(result.stderr.decode())
