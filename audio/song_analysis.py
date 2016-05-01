#!/usr/bin/python

import numpy
from scipy import signal
from matplotlib import pyplot as pyplot
import audio_scraper
import decision_tree as tree
import training_data
from audio.pymir.AudioFile import AudioFile
import pyaudio


def analyze(video_id):
    file_name = audio_scraper.download_song(video_id)
    decision_tree = tree.generate()
    audio_file = AudioFile.open(file_name)
    frames = audio_file.frames(16384)
    analysis = []

    for frame in frames:
        frequencies, levels = get_power_spectrum(frame)
        data = training_data.generate(frequencies, levels)

        try:
            analysis.append(decision_tree.predict(data))
        except ValueError as e:
            print "Encountered error: {0}".format(e)

    return analysis, frames


def get_power_spectrum(frame):
    spectrum, freqs, bins, _ = pyplot.specgram(frame, NFFT=512,
                                               window=signal.hanning(512), Fs=44100)
    levels = -(numpy.log10(numpy.mean(spectrum, axis=1)) ** 2) / 5
    return freqs, levels


def play(analysis, frames):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

    for i in range(0, len(frames)):
    # Write the audio data to the stream
        audioData = frames[i].tostring()
        stream.write(audioData)
        print analysis[i]

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

