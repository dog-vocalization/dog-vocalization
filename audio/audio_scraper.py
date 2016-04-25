#!/usr/bin/python

import pafy

import os
import subprocess
import re
import time
import glob

AUDIO_DIR = os.getcwd() + "/audio/audio_files/"
PLAYLIST_SEEDS = {
    "happy": "wrvqHw4wE_Q",
    "angry": "orEC1_Un_1w"
}

def get_audio(audio_dir = AUDIO_DIR):

    audio_files = {}
    for mood, video_id in PLAYLIST_SEEDS.iteritems():
        audio_files[mood] = glob.glob(audio_dir + mood.upper() + '*.wav')
        if len(audio_files[mood]) is 0:
            audio_files = download_audio()
            return audio_files

    return audio_files


"""
Wrapper for download_playlist that passes each distinct seed and groups it by
the associated mood

Returns the dictionary audio_files, mapping a mood to a list of associated audio
"""
def download_audio(audio_dir = AUDIO_DIR):

    audio_files = {}

    for mood, video_id in PLAYLIST_SEEDS.iteritems():
        audio_files[mood] = [] #not sure if this line is necessary
        
        wav_files = download_playlist(mood, video_id)
        audio_files[mood] = wav_files

    print "\n********** Finished downloading audio files \n"
    return audio_files


"""
Download's the audio of a YT mix playlist based on a seed video id

Returns the list of converted audio files that were downloaded.
"""
def download_playlist(mood, video_id, audio_dir = AUDIO_DIR):

    #use seed_video to generate mix playlist id
    seed_video = pafy.new(video_id)
    playlist_id = seed_video.mix.plid
    
    #create a playlist meta object from the playlist id
    #extract list of video urls from playlist meta object
    playlist_and_meta = pafy.get_playlist(playlist_id)
    playlist = playlist_and_meta['items']
    
    wav_files = []
            
    #iterate over list of video urls to download their audio    
    for x in xrange(-1,len(playlist)):
        
        #process seed video first
        if x == -1:
            video = pafy.new(video_id)
        #then process playlist videos generated by seed video
        else:
            video = playlist[x]['pafy']      
        
        #select stream with the best m4a audio
        stream = video.getbestaudio(preftype="m4a")
        title = re.sub(r'\W+', '', video.title.replace (" ", "_"))

        #initialize local audio file paths
        m4a_file = audio_dir + mood.upper() + "_" + title + "." + stream.extension
        wav_file = m4a_file[:-4] + '.wav'
        
        #if file doesn't already exist, download it from stream
        if not (os.path.isfile(m4a_file) or os.pathisfile(wav_file)):
            m4a_file = stream.download(filepath = m4a_file)
            
        #if file isn't already converted, convert it to wav        
        if not os.path.isfile(wav_file):
            wav_file = convert_to_wav(m4a_file)


        wav_files.append(wav_file)
        print "Downloaded {0}\n".format(wav_file)
    
    return wav_files


"""
Relies on users' FFMPEG install to convert m4a to wav
User MUST have FFMPEG installed on their system path/system environ variables

!CAUTION!: If this is being run in an IDE, make sure the **IDE** has visibility
to system PATH variables in order to properly run FFMPEG.

Returns path to new wav file.
"""
def convert_to_wav(m4a_file,audio_dir = AUDIO_DIR):
    
    ffmpeg_bin = "ffmpeg"
    wav_file = m4a_file[:-4] + '.wav'
    
    command = [ ffmpeg_bin, '-i', m4a_file, wav_file, '-y' ]
    conversionProcess = subprocess.Popen(command, stdout = subprocess.PIPE)          
    
    # Wait until we're done converting the file
    while os.path.isfile(wav_file) is False:
        time.sleep(1)
    conversionProcess.stdout.close()

    # Delete the m4a file
    try:
        os.remove(m4a_file)
    except:
        print "unable to remove old m4a file..."
    
    return wav_file

