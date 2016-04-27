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
            ffts.append(frame.mean())

        return numpy.mean(ffts)


    def spectral_rolloff(self):
        spectral_rolloffs = []
        for frame in self.audio_frames:
            spectral_rolloffs.append(frame.spectral_rolloff())

        return numpy.mean(spectral_rolloffs)

    def spectral_flatness(self):
        spectral_flatnesses = []
        for frame in self.audio_frames:
            spectral_flatnesses.append(frame.spectral_flatness())

        return numpy.mean(spectral_flatnesses)

    def rms(self):
        rmses = []
        for frame in self.audio_frames:
            rmses.append(frame.rms())

        return numpy.mean(rmses)

    def mean(self):
        means = []
        for frame in self.audio_frames:
            means.append(frame.mean())

        return numpy.mean(means)

    def variance(self):
        variances = []
        for frame in self.audio_frames:
            variances.append(frame.variance())

        return numpy.mean(variances)

    def generate_dataset(self):
        dataset = [
            self.fft(),
            self.spectral_rolloff(),
            self.spectral_flatness(),
            self.rms(),
            self.mean(),
            self.variance()
        ]

        return dataset


