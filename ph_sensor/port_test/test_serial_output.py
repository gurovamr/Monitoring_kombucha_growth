import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2)
time.sleep(2)

print("Listening for messages...\n")

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode(errors='ignore').strip()
            print(f"Arduino says: {line}")
except KeyboardInterrupt:
    print("Stopped.")
finally:
    ser.close()
