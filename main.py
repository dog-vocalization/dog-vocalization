#!/usr/bin/python

import audio.song_analysis as song_analysis
#import audio.audio_scraper as audio_scraper

 
if __name__ == "__main__":
    #audio_scraper.test_audio_scraper()

    analysis, frames = song_analysis.analyze("orEC1_Un_1w")
    # print analysis
    song_analysis.play(analysis, frames)



