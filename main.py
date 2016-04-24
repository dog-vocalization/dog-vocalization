#!/usr/bin/python

import audio.audio_scraper as audio_scraper
from audio.audio_mood import AudioMood


if __name__ == "__main__":
    audio_files = audio_scraper.get_audio()

    for mood_category, data in audio_files.iteritems():

        mood = AudioMood(mood_category, data)
        mood.run_analysis()



