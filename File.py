import sys
import cv2
import time
import threading

class File(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def setParam(self, width=640, height=480, quality=50, source='video.mp4'):
        self.__dim = (width, height)
        self.__file = cv2.VideoCapture(source)
        self.__fps = 1 / self.__file.get(cv2.CAP_PROP_FPS)
        self.__encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        self.__frame = b''

    def run(self):
        while(self.__file.isOpened()):
            start = time.time()
            ret, frame = self.__file.read()
            if ret:
                frame = cv2.resize(frame, self.__dim, interpolation = cv2.INTER_CUBIC)
                ret, buffer = cv2.imencode('.jpg', frame,self.__encode_param)
                frame = buffer.tobytes()
                self.__frame = frame
            else:
                self.__file.set(cv2.CAP_PROP_POS_FRAMES, 0)
            diff = time.time() - start
            while  diff < self.__fps:
                diff = time.time() - start
            
        self.__file.release()

    def getFrame(self):
        return self.__frame
        
        
