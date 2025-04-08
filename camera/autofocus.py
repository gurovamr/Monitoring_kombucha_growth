import subprocess
import cv2
import os
from datetime import datetime

def is_blurry(image_path, threshold=100.0):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return True
    lap_var = cv2.Laplacian(img, cv2.CV_64F).var()
    print(f"Laplacian variance: {lap_var:.2f}")
    return lap_var < threshold

# Capture image with autofocus
timestamp = datetime.now().strftime("%m-%d_%H-%M")
img_path = f"/home/gurov/Monitoring_kombucha_growth/data/test/focus_test_{timestamp}.jpg"

result = subprocess.run([
    "libcamera-still", 
    "--camera", "0", 
    "--autofocus-mode", "auto",
    "--timeout", "3000",  # time for focusing
    "-o", img_path
], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if os.path.exists(img_path):
    print(f"Image saved to {img_path}")
    if is_blurry(img_path):
        print("⚠️ Image is blurry.")
    else:
        print("✅ Image is sharp.")
else:
    print("Image capture failed.")
    print(result.stderr.decode())
