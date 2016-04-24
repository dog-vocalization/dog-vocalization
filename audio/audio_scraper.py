#!/usr/bin/python

import pafy
import os
import subprocess
import re
import time
import glob

AUDIO_DIR = os.getcwd() + "/audio_files/"
PLAYLIST_SEEDS = {
    "happy": "wrvqHw4wE_Q",
    "angry": "orEC1_Un_1w"
}


def get_audio():

    audio_files = {}
    for mood, video_id in PLAYLIST_SEEDS.iteritems():
        audio_files[mood] = glob.glob(AUDIO_DIR + mood.upper() + '*.wav')
        if len(audio_files[mood]) is 0:
            audio_files = download_audio()
            return audio_files

    return audio_files


def download_audio():

    audio_files = {}

    for mood, video_id in PLAYLIST_SEEDS.iteritems():
        audio_files[mood] = []

        video = pafy.new(video_id)
        stream = video.getbestaudio(preftype="m4a")

        title = re.sub(r'\W+', '', video.title.replace (" ", "_"))
        file_path = AUDIO_DIR + mood.upper() + "_" + title + "." + stream.extension

        file = stream.download(filepath = file_path)
        file_name = convert_to_wav(file)
        audio_files[mood].append(file_name)

        file_names = download_playlist(mood, video.mix.plid)
        audio_files[mood].extend(file_names)

    print "\n********** Finished downloading audio files \n"
    return audio_files


def download_playlist(mood, video_id):

    #create a playlist meta object from the playlist id
    playlist_and_meta = pafy.get_playlist(video_id)

    #extract list of video urls from playlist meta object
    playlist = playlist_and_meta['items']

    #iterate over list of video urls and download their audio
    for x in xrange(len(playlist)):
        video = playlist[x]['pafy']
        stream = video.getbestaudio(preftype="m4a")

        title = re.sub(r'\W+', '', video.title.replace (" ", "_"))
        file_path = AUDIO_DIR + mood.upper() + "_" + title + "." + stream.extension

        file = stream.download(filepath = file_path)
        file_name = convert_to_wav(file)
        print "Downloaded {0}".format(file[:-4] + '.wav')
        return file_name


def convert_to_wav(file_path):
    ffmpeg_bin = "ffmpeg"
    if os.name == "nt": ffmpeg_bin += ".exe" # format for Windows machines

    new_file_path = file_path[:-4] + '.wav'

    command = [ ffmpeg_bin, '-i', file_path, new_file_path, '-y' ]
    conversionProcess = subprocess.Popen(command, stdout = subprocess.PIPE)

    # Wait until we're done converting the file
    while os.path.isfile(new_file_path) is False:
        time.sleep(1)

    conversionProcess.stdout.close()

    # Delete the m4a files
    command = [ 'find', AUDIO_DIR, '-name', '*.m4a', '-exec', 'rm', '-rf', '{}', ';' ]
    deletionProcess = subprocess.Popen(command, stdout = subprocess.PIPE)

    # Wait until we're done deleting the old file
    while os.path.isfile(file_path) is True:
        time.sleep(1)

    deletionProcess.stdout.close()
    return new_file_path



