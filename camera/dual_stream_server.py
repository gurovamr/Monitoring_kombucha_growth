from flask import Flask, Response, render_template_string
from picamera2 import Picamera2
import time
import cv2

app = Flask(__name__)

# Initialize camera 0
cam0 = Picamera2(camera_num=0)
cam0_config = cam0.create_video_configuration(main={"size": (2304, 1296), "format": "RGB888"})
cam0.configure(cam0_config)

# Enable continuous autofocus for cam0
cam0.set_controls({"AfMode": 2})  # 2 = Continuous AF

cam0.start()
time.sleep(2)  # Give time for camera to start

# Initialize camera 1
cam1 = Picamera2(camera_num=1)
cam1_config = cam1.create_video_configuration(main={"size": (2304, 1296), "format": "RGB888"})
cam1.configure(cam1_config)

# Enable continuous autofocus for cam1
cam1.set_controls({"AfMode": 2})  # 2 = Continuous AF

cam1.start()
time.sleep(2)

# Stream generator
def gen_frames(cam):
    while True:
        frame = cam.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# Routes for streaming
@app.route('/cam0')
def stream_cam0():
    return Response(gen_frames(cam0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam1')
def stream_cam1():
    return Response(gen_frames(cam1), mimetype='multipart/x-mixed-replace; boundary=frame')

# HTML viewer
@app.route('/')
def viewer():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Dual Camera Viewer</title>
      <style>
        body {
          background-color: #000;
          color: white;
          font-family: sans-serif;
          display: flex;
          flex-direction: row;
          justify-content: center;
          gap: 40px;
          padding: 20px;
        }
        .cam {
          text-align: center;
        }
        img {
          border: 2px solid white;
          max-width: 100%;
          height: auto;
        }
      </style>
    </head>
    <body>
      <div class="cam">
        <img src="/cam0" alt="Camera 0">
        <p>Camera 0</p>
      </div>
      <div class="cam">
        <img src="/cam1" alt="Camera 1">
        <p>Camera 1</p>
      </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
