#!/usr/bin/python

from pymir import Transforms


"""
AudioFrame defines the attributes of each subdivision of an audio file, called a
"frame".  These attributes keep track of potential audio "feature selections".
(a.k.a. tracks the future useful transformations on the frame's FFT).
"""
class AudioFrame():

    def __init__(self, frame):
        self.frame = frame
        # This is an instance of the Spectrum class
        self.fft = Transforms.fft(self.frame)

    def fft_data(self):
        return self.fft

    def spectral_rolloff(self):
        return self.fft.rolloff()

    def spectral_flatness(self):
        return self.fft.flatness()

    def rms(self):
        return self.frame.rms()

    def mean(self):
        return self.fft.mean()

    def variance(self):
        return self.fft.variance()

    def data(self):
        data = {
            'fft': self.fft(),
            'spectral_rolloff': self.spectral_rolloff(),
            'spectral_flatness': self.spectral_flatness(),
            'rms': self.rms(),
            'mean': self.mean(),
            'variance': self.variance()
        }

        return data

    def plot(self):
        return self.audio_file.frame.plot()

