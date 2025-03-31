import os
from datetime import datetime
import subprocess

# Save path
save_dir = "/home/gurov/Monitoring_kombucha_growth/data"

# Get timestamp 
timestamp = datetime.now().strftime("%m-%d_%H-%M")

cam0_file = f"{save_dir}/cam0_{timestamp}.jpg"
cam1_file = f"{save_dir}/cam1_{timestamp}.jpg"

# Run libcamera-still for both cameras
subprocess.run(["libcamera-still", "--camera", "0", "-o", cam0_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["libcamera-still", "--camera", "1", "-o", cam1_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Images captured:", cam0_file, cam1_file)
