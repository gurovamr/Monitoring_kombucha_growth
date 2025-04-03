import serial
import time

port = '/dev/ttyACM0'
baud = 115200

try:
    ser = serial.Serial(port, baud, timeout=2)
    time.sleep(10)
    print("Reading pH values...\n")

    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print("Current", line)

except serial.SerialException as e:
    print("Serial error:", e)
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
