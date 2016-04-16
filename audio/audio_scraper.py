#!/usr/bin/python

import pafy
import os
import subprocess

RESULT_DIR = os.getcwd() + "/audio_files/"
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
        file_path = RESULT_DIR + mood.upper() + "_" + title + "." + stream.extension

        file = stream.download(filepath = file_path)
        print "Downloaded {0}".format(file)

        download_playlist(mood, video.mix.plid)

    print "\n--------------- Finished downloading audio files ---------------\n"
    convert_to_wav()
    print "\n--------------- Finished converting audio files from .m4a to .wav ---------------\n"


def download_playlist(mood, video_id):
    playlist_and_meta = pafy.get_playlist(video_id)
    playlist = playlist_and_meta['items']


    for x in xrange(len(playlist)):
        video = playlist[x]['pafy']
        stream = video.getbestaudio(preftype="m4a")

        title = video.title.replace (" ", "_").encode('utf-8')
        file_path = RESULT_DIR + mood.upper() + "_" + title + "." + stream.extension

        file = stream.download(filepath = file_path)
        print "Downloaded {0}".format(file)


def convert_to_wav():
    ffmpeg_bin = "ffmpeg"
    if os.name == "nt": ffmpeg_bin += ".exe" # format for Windows machines

    for file_name in os.listdir(RESULT_DIR):
        # Bash command to convert .m4a to .wav using FFMPEG
        command = [
            ffmpeg_bin, # FFMPEG location
            '-nostats', '-loglevel', '0', # tell FFMPEG to be quiet!!
            '-i', RESULT_DIR + file_name, # -i indicates the input file
            '-acodec', # force audio codec
            'pcm_s16le', # PCM means "traditional wave like format" (raw bytes, basically). 16 means 16 bits per sample, "le" means "little endian"
            RESULT_DIR + file_name[:-4] +'.wav', # output file
            '-y', # yes to overriding existing files with the same name
            '-' # let FFMPEG know its being used outside command line
        ]
        subprocess.Popen(command, stdout = subprocess.PIPE)

    # Delete the m4a files
    command = [ 'find', RESULT_DIR, '-name', '*.m4a', '-exec', 'rm', '-rf', '{}', ';' ]
    subprocess.Popen(command, stdout = subprocess.PIPE)



