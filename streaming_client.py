import sys
import cv2
import numpy as np
import urllib.request
import argparse

def connect(url):
    try:   
        stream = urllib.request.urlopen(url)
    except:
        sys.exit("Bad address/can't connect")
    else:
        print("Connected to: " + url)
    
    return stream 

def main(url):  
    stream = connect(url)
    bytes = b''
    while True:
        try:
            bytes += stream.read(2048)
            a = bytes.find(b'\xff\xd8')
            b = bytes.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes[a:b+2]
                bytes = bytes[b+2:]
                frame = cv2.imdecode(np.frombuffer(jpg, np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow('Video Stream', frame)
        except:
            cv2.destroyAllWindows()
            sys.exit("Connection error")

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            sys.exit()

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-u', action="store", dest="url", default='http://localhost/video', type=str)
parser.add_argument('-f', action="store", dest="framerate", default=30, type=float)
args = parser.parse_args()

if __name__ == "__main__":
    main(args.url+'?f='+str(args.framerate))
