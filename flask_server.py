from flask import Flask, render_template, Response
import time
import Camera

app = Flask(__name__)
cam = Camera.Camera(640,480,15)

def get_frames():  
    while True:       
            time.sleep(.033) 
            yield (cam.getFrame())             

@app.route('/video')
def video():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    cam.start()
    app.run(host='0.0.0.0',port=80)

    
