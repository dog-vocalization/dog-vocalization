#!/usr/bin/python

import audio.song_analysis as song_analysis


if __name__ == "__main__":
    analysis, frames = song_analysis.analyze("orEC1_Un_1w")
    # print analysis
    song_analysis.play(analysis, frames)



