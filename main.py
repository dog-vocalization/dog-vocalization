#!/usr/bin/python

import audio.song_analysis as song_analysis
import audio.audio_scraper as audio_scraper

import os
import sys

#used to suppress deprecation error messages in sklearn package
class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr
 
if __name__ == "__main__":
    #audio_scraper.test_audio_scraper()

    devnull = open(os.devnull, 'w')

    with RedirectStdStreams(stderr=devnull):
        analysis, frames = song_analysis.analyze("orEC1_Un_1w")

    #analysis, frames = song_analysis.analyze("orEC1_Un_1w")
    #print analysis
    song_analysis.play(analysis, frames)



