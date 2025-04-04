import os
from datetime import datetime
import subprocess
import time

save_dir = "/home/gurov/Monitoring_kombucha_growth/data"
timestamp = datetime.now().strftime("%m-%d_%H-%M")

cam0_file = f"{save_dir}/cam0_{timestamp}.jpg"
cam1_file = f"{save_dir}/cam1_{timestamp}.jpg"

# Capture cam0
result0 = subprocess.run(["libcamera-still", "--camera", "0", "-o", cam0_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(25)  
# Capture cam1
result1 = subprocess.run(["libcamera-still", "--camera", "1", "-o", cam1_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Check and log results
success = []
if os.path.exists(cam0_file):
    success.append("cam0")
else:
    print("cam0 image not saved")
    print(result0.stderr.decode())

if os.path.exists(cam1_file):
    success.append("cam1")
else:
    print("cam1 image not saved")
    print(result1.stderr.decode())

print(f"Images captured: {', '.join(success)} at {timestamp}")
