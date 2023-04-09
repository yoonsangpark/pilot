# pilot

1. gst_rtsp_server.py
  gst-launch-1.0 playbin uri=rtsp://192.168.10.104:8554/test
  or
  rtsp://192.168.10.104:8554/test
  
  
2. gst_rtsp_server_cam.py
  gst-launch-1.0 -v playbin uri=rtsp://192.168.10.104:8554/test uridecodebin0::source::latency=300
  or
  rtsp://192.168.10.104:8554/test
