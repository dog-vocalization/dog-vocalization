#!/usr/bin/python

import numpy
from scipy import signal
from matplotlib import pyplot as pyplot

import audio_scraper
import decision_tree
import training_data

from audio.pymir.AudioFile import AudioFile

import os
import time


class SongAnalyzer():

    def __init__(self, video_id):
        self.file_name = audio_scraper.download_song(video_id)
        self.decision_tree = decision_tree.generate()
        self.audiofile = AudioFile.open(self.file_name)
        self.frames =  self.audiofile.frames(16384)

    def file_name(self):
        return self.file_name

    def analyze(self):
        analysis = []

        for frame in self.frames:
            frequencies, levels = self.get_power_spectrum(frame)
            analyzer = training_data.generate(frequencies, levels)
            data = analyzer.training_data()

            try:
                analysis.append(self.decision_tree.predict(data))
            except ValueError as e:
                print "Encountered error: {0}".format(e)

        return analysis

    def get_power_spectrum(self, frame):
        spectrum, freqs, bins, _ = pyplot.specgram(frame, NFFT=512,
                                            window=signal.hanning(512), Fs=44100)
        levels = -(numpy.log10(numpy.mean(spectrum, axis=1)) **2)/5
        return freqs, levels


    # This is used to generate a text file with the frequencies and levels, as well as the
    # manually determined categorization, for a clip of size 16384. Right now it isn't being used
    # anywhere, but if we want to add more data to the audio_data folder, we can call it on each
    # frame belonging to this class to do so
    def import_data(self, frame):
        frame.play()

        category = raw_input("Type b for bark, g for growl, or x for background (or s to skip): ")
        category_array = { 'b': 'bark', 'g': 'growl', 'x':'background', 's': 'skip' }
        category = category_array[category]
        if category == 'skip':
            return

        frequencies, levels = self.get_power_spectrum(frame)
        file_name = "{0}/audio/audio_data/{1}_{2}.txt".format(os.getcwd(), category, time.time())

        with open(file_name, 'a') as new_file:
            new_file.write(category + "\n")
            for i in range(0, len(frequencies)):
                new_file.write("{0},{1}\n".format(frequencies[i], levels[i]))

            new_file.close()