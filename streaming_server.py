from flask import Flask, render_template, Response, request
import time
import Camera
import File
import argparse

app = Flask(__name__)


def get_frames(f):  
    while True:
        start = time.time()
        diff = time.time() - start
        while  diff < 1/f:
            diff = time.time() - start
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + source.getFrame() + b'\r\n' )             

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
parser.add_argument('-f', action="store_true", dest="file")
parser.add_argument('-s', action="store", dest="source")
parser.add_argument('-p', action="store", dest="port", default=80, type=int)
args = parser.parse_args()

if __name__ == '__main__':
    if args.file:
        source = File.File()
    else:
        source = Camera.Camera()
        args.source = int(args.source)

    source.setParam(args.width, args.height, args.quality, args.source)
    source.start()
    app.run(host='0.0.0.0',port=args.port)

    
