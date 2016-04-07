#!/usr/bin/python

import microphone_util
import time

DEVICE_NAME = "USB Audio Device"

class Microphone(object):
    def __init__(self):
        self.listener = microphone_util.Listener()

    def run(self):
        self.listener.set_stream(DEVICE_NAME)
        self.listener.observe()


    def stop(self):
        self.listener.stop()


if __name__ == "__main__":
    microphone = Microphone()
    microphone.run()
