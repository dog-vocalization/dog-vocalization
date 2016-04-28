#!/usr/bin/python

import numpy
from scipy import signal
from matplotlib import pyplot as pyplot

import audio_scraper
import audio_analysis
from spectrum_analysis import SpectrumAnalyzer

from audio.pymir.AudioFile import AudioFile


class SongAnalyzer():

    def __init__(self, video_id):
        self.file_name = audio_scraper.download_song(video_id)
        self.decision_tree = audio_analysis.build_decision_tree()

        self.audiofile = AudioFile.open(self.file_name)
        self.frames =  self.audiofile.frames(2048, numpy.hamming)

    def file_name(self):
        return self.file_name

    def get_power_spectrum(self, frame):
        pxx, freqs, bins, _ = pyplot.specgram(frame, NFFT=512,
                                              window=signal.hanning(512), Fs=44100)

        levels = 20 * numpy.log10(numpy.mean(pxx, axis=1))
        return freqs, levels

    def analyze(self):

        analysis = []

        for frame in self.frames:
            freqs, levels = self.get_power_spectrum(frame)

            analyzer = SpectrumAnalyzer([ freqs, levels ])
            data = analyzer.training_data()

            try:
                analysis.append(self.decision_tree.predict(data[:-2]))
            except ValueError as e:
                print "Encountered error: {0}".format(e)

        return analysis
