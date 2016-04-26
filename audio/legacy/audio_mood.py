#!/usr/bin/python
import os

from numpy import nan_to_num
from audio_file import File

import matplotlib.pyplot as pyplot
import time

class AudioMood():

    def __init__(self, mood, file_names):
        self.mood = mood
        self.files = self.get_audio_files(file_names)

    def get_audio_files(self, file_names):

        files = []
        for file_name in file_names:
            audio_file = File(file_name)
            files.append(audio_file)

        return files

    def generate_dataset(self):

        datasets = []
        all_data = []

        for audio_file in self.files:
            dataset = audio_file.generate_dataset()

            dataset = nan_to_num(dataset)
            datasets.append(dataset)
            all_data.extend(dataset)

            output = "Finished generating dataset for {0}: {1}\n".format(audio_file.file_name, dataset)
            print output

        pyplot.plot(all_data)

        pyplot.savefig(os.getcwd() + '/image_files/{0}_mood.png'.format(time.time()), bbox_inches='tight')
        pyplot.close()
        return datasets


