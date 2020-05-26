from flask import Flask, render_template, Response, request
import time
import Camera
import argparse

app = Flask(__name__)
cam = Camera.Camera()

def get_frames(f):  
    while True:       
            time.sleep(1/f) 
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + cam.getFrame() + b'\r\n' )             

@app.route('/video')
def video():
    f = request.args.get('f',default=30, type=float)
    return Response(get_frames(f), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-w', action="store", dest="width", default=640, type=int)
parser.add_argument('-h', action="store", dest="height", default=480, type=int)
parser.add_argument('-q', action="store", dest="quality", default=50, type=int)
parser.add_argument('-s', action="store", dest="source", default=0, type=int)
parser.add_argument('-p', action="store", dest="port", default=80, type=int)
args = parser.parse_args()

if __name__ == '__main__':
    cam.setParam(args.width, args.height, args.quality, args.source)
    cam.start()
    app.run(host='0.0.0.0',port=args.port)

    
