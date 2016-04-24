#!/usr/bin/python

from numpy import isnan
from audio_file import File


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
        for audio_file in self.files:
            dataset = audio_file.generate_dataset()

            where_are_NaNs = isnan(dataset)
            dataset[where_are_NaNs] = 0

            datasets.append(dataset)

            output = "Finished generating dataset for {0}: {1}\n".format(audio_file.file_name, dataset)
            print output

        return dataset


