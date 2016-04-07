#!/usr/bin/python

import pyaudio
import struct
import math

INITIAL_BARK_THRESHOLD = 0.0002
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0/32768.0)
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
BARKING_THRESHOLD = 6.56140401817e-05

def get_rms( block ):
    # RMS amplitude is defined as the square root of the
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into
    # a string of 16-bit samples...

    # we will get one short out for each
    # two chars in the string.
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768.
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class Listener(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.bark_threshold = INITIAL_BARK_THRESHOLD
        self.errorcount = 0


    def stop(self):
        self.stream.close()


    def set_stream(self, device_name = None):
        self.stream = self.open_mic_stream(device_name)


    def find_input_device(self, device_name = None):

        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)

            if device_name is None or devinfo["name"] == device_name:
                print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                return { 'index': i, 'channels': devinfo['maxInputChannels']}

        # If we reached here, we have a problem
        print( "Could not find input device. Please make sure your microphone is set up correctly." )



    def open_mic_stream(self, device_name = None):
        device_info = self.find_input_device(device_name)

        stream = self.pa.open(   format = FORMAT,
                                 channels = device_info['channels'],
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_info['index'],
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)
        return stream


    def listen(self):

        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        except IOError, e:
            # dammit.
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )

        amplitude = get_rms( block )
        return amplitude


    def get_silence(self):

        amplitudes = []
        for i in range(1000):
            amplitudes.append(self.listen())

        silence_min = min(amplitudes)
        silence_max = max(amplitudes)
        print "Silence min: {0}, silence max: {1}, silence average: {2}".format(silence_min, silence_max, reduce(lambda x, y: x + y, amplitudes) / len(amplitudes))

    def get_barking(self):

        amplitudes = []
        for i in range(1000):
            amplitudes.append(self.listen())

        barking_min = min(amplitudes)
        barking_max = max(amplitudes)
        print "Barking min: {0}, barking max: {1}, avg: {2}".format(barking_min, barking_max, reduce(lambda x, y: x + y, amplitudes) / len(amplitudes))


    def observe(self):
        for i in range(1000):
            amplitude = self.listen()
            if amplitude > BARKING_THRESHOLD:
                print "{0} BARKING".format(i)