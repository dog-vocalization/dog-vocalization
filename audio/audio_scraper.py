#!/usr/bin/python

import pafy
import os
import subprocess
import re
import signal
import fnmatch

RESULT_DIR = os.getcwd() + "/audio_files/"
#BASE_URL = "https://www.youtube.com/watch?v=" #this is unnecessary
PLAYLIST_SEEDS = {
    "happy": "wrvqHw4wE_Q",
    "angry": "orEC1_Un_1w"
}


def get_audio():
    for mood, video_id in PLAYLIST_SEEDS.iteritems():

        #video = pafy.new(BASE_URL + video_id)
        video = pafy.new(video_id)
        stream = video.getbestaudio(preftype="m4a")

        title = re.sub(r'\W+', '', video.title.replace (" ", "_"))
        file_path = RESULT_DIR + mood.upper() + "_" + title + "." + stream.extension

        file = stream.download(filepath = file_path)
        print "Downloaded {0}".format(file)

        download_playlist(mood, video.mix.plid)

    print "\n********** Finished downloading audio files \n"
    convert_to_wav()
    print "\n********** Finished converting audio files from .m4a to .wav \n"


def download_playlist(mood, playlist_id):

    #create a playlist meta object from the playlist id
    playlist_and_meta = pafy.get_playlist(playlist_id)

    #extract list of video urls from playlist meta object
    playlist = playlist_and_meta['items']

    #iterate over list of video urls and download their audio
    for x in xrange(len(playlist)):
        video = playlist[x]['pafy']
        stream = video.getbestaudio(preftype="m4a")

        title = re.sub(r'\W+', '', video.title.replace (" ", "_"))
        file_path = RESULT_DIR + mood.upper() + "_" + title + "." + stream.extension

        file = stream.download(filepath = file_path)
        print "Downloaded {0}".format(file)


def convert_to_wav():
    ffmpeg_bin = "ffmpeg"
    if os.name == "nt": ffmpeg_bin += ".exe" # format for Windows machines

    for file_name in (file for file in os.listdir(RESULT_DIR) if fnmatch.fnmatch(file, '*.m4a')):
        command = [ ffmpeg_bin, '-loglevel', '0', '-i', RESULT_DIR + file_name, RESULT_DIR + file_name[:-4] +'.wav', '-y' ]
        process = subprocess.Popen(command, stdout = subprocess.PIPE, preexec_fn=os.setsid)

        # Kill the processes when we're done
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)

    # Delete the m4a files
    command = [ 'find', RESULT_DIR, '-name', '*.m4a', '-exec', 'rm', '-rf', '{}', ';' ]
    subprocess.Popen(command, stdout = subprocess.PIPE)



