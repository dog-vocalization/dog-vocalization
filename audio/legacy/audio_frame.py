#!/usr/bin/python

from audio.pymir import Transforms


class AudioFrame():

    def __init__(self, frame):
        self.frame = frame
        # This is an instance of the Spectrum class
        self.fft = Transforms.fft(self.frame)

    def fft_data(self):
        return self.fft.mean() ** 2

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

    def spread(self):
        return self.fft.spread()

    def data(self):
        data = {
            'fft': self.fft(),
            'spectral_rolloff': self.spectral_rolloff(),
            'spectral_flatness': self.spectral_flatness(),
            'rms': self.rms(),
            'mean': self.mean(),
            'variance': self.variance(),
            'spread': self.spread()
        }

        return data

    def plot(self):
        return self.audio_file.frame.plot()

