#!/usr/bin/python

import audio.audio_scraper as audio_scraper
import audio.audio_analysis as audio_analysis


if __name__ == "__main__":
    audio_files = audio_scraper.get_audio()
    audio_analysis.run_analysis(file_name="/training_data.csv")



