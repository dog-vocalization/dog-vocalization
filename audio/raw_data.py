#!/usr/bin/python

import audio_scraper
from audio.pymir.AudioFile import AudioFile
import os
import time
import song_analysis


def import_data(video_id):
    file_name = audio_scraper.download_song(video_id)
    audio_file = AudioFile.open(file_name)
    frames = audio_file.frames(16384)

    for frame in frames:
        import_frame(frame)


# This is used to generate a text file with the frequencies and levels, as well as the
# manually determined categorization, for a clip of size 16384. Right now it isn't being used
# anywhere, but if we want to add more data to the audio_data folder, we can call it on each
# frame belonging to this class to do so
def import_frame(frame):
    frame.play()

    category = raw_input("Type b for bark, g for growl, or x for background (or s to skip): ")
    category_array = {'b': 'bark', 'g': 'growl', 'x': 'background', 's': 'skip'}
    category = category_array[category]
    if category == 'skip':
        return

    frequencies, levels = song_analysis.get_power_spectrum(frame)
    file_name = "{0}/audio/audio_data/{1}_{2}.txt".format(os.getcwd(), category, time.time())

    with open(file_name, 'a') as new_file:
        new_file.write(category + "\n")
        for i in range(0, len(frequencies)):
            new_file.write("{0},{1}\n".format(frequencies[i], levels[i]))

        new_file.close()


