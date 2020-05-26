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
python streaming_server.py -w width -h height -q jpeg_quality -f video_as_source_flag -s source -p port
```

### Dedicated client
```
python streaming_client.py -u feed_url -f framerate
```
Default arguments: -u http&#58;//localhost/video -f 30 

### Web client
Open http&#58;//localhost/ or access direct feed at http&#58;//localhost/video?f=30 for 30fps stream.
