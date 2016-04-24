#!/usr/bin/python

import os
import time

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

    def run_analysis(self):

        results_file = open("{0}/{1}_{2}_results.txt".format(os.getcwd(), self.mood, time.time()), 'w')

        for audio_file in self.files:
            audio_file.fft()
            return

            # data = audio_file.data()


        #     result_text = "********************" + audio_file.file_name + "/n"
        #     for name, value in data:
        #         result_text += name + ": " + value + "\n"
        #
        #     result_text += "\n\n"
        #     results_file.write(result_text)
        #     results_file.close()
        #     return
        #
        # results_file.close()