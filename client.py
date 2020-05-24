import sys
import cv2
import numpy as np
import urllib.request

def connect(url):
    try:   
        stream = urllib.request.urlopen(url)
    except:
        sys.exit("Bad address/can't connect")
        
    return stream 

def main(argv):
    if len(argv) == 1:
        url = argv[0]
    else:
        url = 'http://localhost/video'
    
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
            sys.exit("Connection error")

        if cv2.waitKey(1) == 27:
            exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])
