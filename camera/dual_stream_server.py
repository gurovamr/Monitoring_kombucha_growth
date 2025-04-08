from flask import Flask, Response, render_template_string
from picamera2 import Picamera2
import cv2

app = Flask(__name__)

# Initialize both cameras
cam0 = Picamera2(camera_num=0)
cam0.preview_configuration.main.size = (640, 480)
cam0.preview_configuration.main.format = "RGB888"
cam0.configure("preview")
cam0.start()

cam1 = Picamera2(camera_num=1)
cam1.preview_configuration.main.size = (640, 480)
cam1.preview_configuration.main.format = "RGB888"
cam1.configure("preview")
cam1.start()

def gen_frames(cam):
    while True:
        frame = cam.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/cam0')
def stream_cam0():
    return Response(gen_frames(cam0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam1')
def stream_cam1():
    return Response(gen_frames(cam1), mimetype='multipart/x-mixed-replace; boundary=frame')

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
