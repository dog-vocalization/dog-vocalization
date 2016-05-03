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
    print "Beginning audio analysis...\n"
    file_name = audio_scraper.get_wav_from_vid(video_id)
    decision_tree = tree.generate()
    audio_file = AudioFile.open(file_name)
    frames = audio_file.frames(16384)
    save_spectrum_image(audio_file)

    analysis = []
    i = 0

    for frame in frames:
        #print "Processing [audio frame {}]...".format(i)
        frequencies, levels = get_power_spectrum(frame)
        data = training_data.generate(frequencies, levels, file_name)
        
        try:
            analysis.append(decision_tree.predict(data))
        except ValueError as e:
            print "Encountered error: {0}".format(e)

        i+=1

    print "Audio analysis complete.\n"

    return analysis, frames



def get_power_spectrum(frame):
    spectrum, freqs, bins, _ = pyplot.specgram(frame, NFFT=512,
                                               window=signal.hanning(512), Fs=44100)

    levels = -(numpy.log10(numpy.mean(spectrum, axis=1)) ** 2) / 5
    return freqs, levels

def save_spectrum_image(frame):
    print "Saving power spectrum image..."
    spectrum, freqs, bins, _ = pyplot.specgram(frame, NFFT=512,
                                               window=signal.hanning(512), Fs=44100)
    pyplot.savefig(os.getcwd() + "/image_files/current_song.png")
    print "Save complete.\n"
    
def play(analysis, frames):
    print "Showing live analysis results..."
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
    print "Live analysis complete"


