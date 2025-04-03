# ph_calibrated_verbose.py

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)
time.sleep(2)

print("Starting pH calibration process...\n")

def send_and_read(cmd, wait_time=10):
    ser.write((cmd + '\r\n').encode())
    print(f"Sent: {cmd}")
    timeout = time.time() + wait_time
    while time.time() < timeout:
        while ser.in_waiting:
            response = ser.readline().decode(errors='ignore').strip()
            if response:
                print(f"Response: {response}")
        time.sleep(0.2)

# 1. Enter calibration mode
send_and_read('enterph', wait_time=15)

# 2. Wait for the pH value to stabilize
print("Waiting 30 seconds for pH to stabilize... ")
for i in range(30):
    print(f"...{i+1}s", end='\r')
    time.sleep(1)

# 3. Calibrate current buffer
send_and_read('calph', wait_time=10)

# 4. Exit calibration
send_and_read('exitph', wait_time=5)

ser.close()
print("\n Calibration sequence completed.")
