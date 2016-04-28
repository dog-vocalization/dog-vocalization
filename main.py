#!/usr/bin/python

import audio.audio_scraper as audio_scraper
import audio.audio_analysis as audio_analysis
from audio.song_analysis import SongAnalyzer


if __name__ == "__main__":
    # audio_files = audio_scraper.get_audio()
    # audio_analysis.analyze()
    song_analysis = SongAnalyzer("dBl76lmp-d0")
    analysis = song_analysis.analyze()
    print analysis



