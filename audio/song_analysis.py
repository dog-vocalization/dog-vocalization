#!/usr/bin/python

import os

import numpy
from scipy import signal
from matplotlib import pyplot as pyplot

from audio.pymir.AudioFile import AudioFile
import pyaudio

import audio_scraper
import decision_tree as tree
import training_data


def analyze(video_id):
    print("aaaa")
    file_name = audio_scraper.get_wav_from_vid("orEC1_Un_1w")
    decision_tree = tree.generate()
    audio_file = AudioFile.open(file_name)
    frames = audio_file.frames(16384)
    save_spectrum_image(audio_file)

    analysis = []

    for frame in frames:
        frequencies, levels = get_power_spectrum(frame)
        data = training_data.generate(frequencies, levels, file_name)

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

def save_spectrum_image(frame):
    spectrum, freqs, bins, _ = pyplot.specgram(frame, NFFT=512,
                                               window=signal.hanning(512), Fs=44100)
    pyplot.savefig(os.getcwd() + "/image_files/current_song.png")

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

