#!/usr/bin/python

import matplotlib.pyplot as pyplot
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
import os
import fnmatch


AUDIO_DIR = os.getcwd() + "/audio_files/"
IMAGE_DIR = os.getcwd() + "/image_files/"

def plot():

    for file_name in (file for file in os.listdir(AUDIO_DIR) if fnmatch.fnmatch(file, '*.wav')):
        fs, data = wavfile.read(AUDIO_DIR + file_name) # load the data
        a = data.T[0] # this is a two channel soundtrack, I get the first track
        try:
            b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
            print b
        except TypeError:
            print "Type error encountered for file " + file_name
            continue

        c = fft(b) # create a list of complex number
        d = len(c)/2  # you only need half of the fft list
        pyplot.plot(abs(c[:(d-1)]),'r')
        savefig(IMAGE_DIR + file_name[:-4] + '.png', bbox_inches='tight')

        print file_name

