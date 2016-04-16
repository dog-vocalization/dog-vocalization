#!/usr/bin/python

import pafy
import os

RESULT_FOLDER = "/happy_audio_files"
BASE_URL = "https://www.youtube.com/watch?v="

VIDEO_IDS = {
    "happy": "wrvqHw4wE_Q",
    "angry": "orEC1_Un_1w"
}


def get_audio():
    for mood, video_id in VIDEO_IDS.iteritems():

        video = pafy.new(BASE_URL + video_id)
        stream = video.getbestaudio(preftype="m4a")

        title = video.title.replace (" ", "_").encode('utf-8')
        file_path = "{0}/audio_files/{1}_{2}.{3}".format(os.getcwd(), mood.upper(), title, stream.extension)

        file = stream.download(filepath = file_path)
        print "Downloaded {0}".format(file)
        download_playlist(mood, video.mix.plid)
    print "--------------- Finished downloading audio_ files ---------------"


def download_playlist(mood, video_id):
    playlist_and_meta = pafy.get_playlist(video_id)
    playlist = playlist_and_meta['items']


    for x in xrange(len(playlist)):
        video = playlist[x]['pafy']
        stream = video.getbestaudio(preftype="m4a")

        title = video.title.replace (" ", "_").encode('utf-8')
        file_path = "{0}/audio_files/{1}_{2}.{3}".format(os.getcwd(), mood.upper(), title, stream.extension)

        file = stream.download(filepath = file_path)
        print "Downloaded {0}".format(file)



get_audio()


