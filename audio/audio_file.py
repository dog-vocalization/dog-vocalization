#!/usr/bin/python

import numpy
import matplotlib.pyplot as pyplot

from pymir.AudioFile import AudioFile
from audio_frame import AudioFrame


class File():

    def __init__(self, file_name):
        self.file_name = file_name
        self.audio_file = AudioFile.open(file_name)

        self.audio_frames = []
        frames = self.audio_file.frames(2048, numpy.hamming)
        for frame in frames:
            self.audio_frames.append(AudioFrame(frame))

    def file_name(self):
        return self.file_name

    def fft(self):

        ffts = []
        for frame in self.audio_frames:
            print frame.mean()
            return
            # ffts.append(frame.fft())

        # pyplot.plot(ffts)
        # pyplot.show()


    def spectral_rolloff(self):
        spectral_rolloffs = []
        for frame in self.audio_frames:
            spectral_rolloffs.append(frame.spectral_rolloff())
        #
        pyplot.plot(spectral_rolloffs)
        pyplot.show()

    def spectral_flatness(self):
        # return self.fft.flatness() TODO

    def rms(self):
        return self.audio_file.frame.rms()

    def mean(self):
        return self.fft.mean()

    def variance(self):
        return self.fft.variance()

    # def data(self):
        # data = {
        #     'fft': self.fft(),
        #     'spectral_rolloff': self.spectral_rolloff(),
        #     'spectral_flatness': self.spectral_flatness(),
        #     'rms': self.rms(),
        #     'mean': self.mean(),
        #     'variance': self.variance()
        # }
        #
        # return data


