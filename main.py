#!/usr/bin/python

import audio.audio_scraper as audio_scraper
import audio.audio_analysis as audio_analysis

def test_audio_scraper():
    wav_files = audio_scraper.download_playlist("test","8QEJDE2WjPA",max_downloads=2)
    m4a_file = audio_scraper.get_m4a("8QEJDE2WjPA")
    wav_file = audio_scraper.convert_to_wav(m4a_file)
    wav_set = audio_scraper.split_audio(wav_files[1])

    print "Files from split: "
    for wav in wav_set:
        print wav


if __name__ == "__main__":
#    test_audio_scraper()
    audio_files = audio_scraper.get_all_audio()
    audio_analysis.run_analysis(file_name="/training_data.csv")



