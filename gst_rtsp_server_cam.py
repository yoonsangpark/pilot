#!/usr/bin/env python
# -*- coding:utf-8 vi:ts=4:noexpandtab
# Simple RTSP server. Run as-is or with a command-line to replace the default pipeline

import sys
import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib

loop = GLib.MainLoop()
#GObject.threads_init()
Gst.init(None)


class MyFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        GstRtspServer.RTSPMediaFactory.__init__(self)

    def do_create_element(self, url):
        pipeline = "v4l2src device=/dev/video0 ! jpegdec ! videoconvert ! queue max-size-buffers=0 max-size-time=0 max-size-bytes=0 min-threshold-time=0 ! x264enc ! video/x-h264,width=640,height=480,framerate=30/1 ! h264parse ! rtph264pay name=pay0 pt=96"    # h264 format -> h264 format
        return Gst.parse_launch(pipeline)

class GstServer():
    def __init__(self):
        self.server = GstRtspServer.RTSPServer()
        f = MyFactory()
        f.set_shared(True)
        m = self.server.get_mount_points()
        m.add_factory("/test", f)
        self.server.attach(None)

if __name__ == '__main__':
        s = GstServer()
        loop.run()
