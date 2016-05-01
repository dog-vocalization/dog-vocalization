#!/usr/bin/python

from audio.song_analysis import SongAnalyzer


if __name__ == "__main__":
    song_analysis = SongAnalyzer("orEC1_Un_1w")
    analysis = song_analysis.analyze()
    print analysis



