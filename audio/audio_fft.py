#!/usr/bin/python

from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *
import os
import fnmatch

AUDIO_DIR = os.getcwd() + "/audio_files/"

def all_ffts(keyword = None):

    results = {}

    for file_name in (file for file in os.listdir(AUDIO_DIR) if fnmatch.fnmatch(file, '*.wav')):
        if keyword is not None or fnmatch.fnmatch(file_name, keyword + '*.wav'):

            try:
                data = fft_data(file_name, keyword)
                results[file_name] = data
            except TypeError:
                print "Type error encountered for file " + file_name

    return results


def fft_data(file_name, keyword = None):

    fs, data = wavfile.read(AUDIO_DIR + file_name) # load the data

    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b) # create a list of complex number
    d = len(c)/2  # you only need half of the fft list

    return c[:(d-1)]


