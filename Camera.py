import sys
import cv2
import threading

class Camera(threading.Thread):
    def __init__(self, width=640, height=480, quality=50, source=0):
        threading.Thread.__init__(self)
        self.__camera = cv2.VideoCapture(source)
        self.__camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.__camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.__encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        self.__frame = b''

    def run(self):
        while(self.__camera.isOpened()):
            ret, frame = self.__camera.read()
            if ret:
                ret, buffer = cv2.imencode('.jpg', frame,self.__encode_param)
                frame = buffer.tobytes()
                self.__frame = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
                

    def getFrame(self):
        return self.__frame
        
        
