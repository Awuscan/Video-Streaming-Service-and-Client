# Video Streaming Service and Client
Apps for university course: Network Services in Business.
Streams webcam image to multiple web/dedicated clients.
Made in Python with OpenCV and Flask.
## Prerequisites
```
pip install opencv-python
pip install flask
```
## Usage
### Server
```
python streaming_server.py -w width -h height -q jpeg_quality -s source_index -p port
```
Default arguments: -w 640 -h 480 -q 50 -s 0 -p 80

### Dedicated client
```
python streaming_client.py -u feed_url -f framerate
```
Default arguments: -u http://localhost/video -f 30 

### Web client
Open http://localhost/ or access direct feed at http://localhost/video?f=<framerate>
