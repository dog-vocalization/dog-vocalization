#!/usr/bin/python

import pafy
from pydub import AudioSegment

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

"""
Iterate over playlist seeds to collect or download all audio to audio_dir.

Returns the list of audio file paths collected from audio_dir.
"""
def get_all_audio(audio_dir = AUDIO_DIR):

    audio_files = {}
    for mood, video_id in PLAYLIST_SEEDS.iteritems():
        audio_files[mood] = glob.glob(audio_dir + mood.upper() + '*.wav')
        if len(audio_files[mood]) is 0:
            audio_files = download_all_audio()

    return audio_files

"""
Wrapper for download_playlist that passes each distinct seed and groups it by
the associated mood

Returns the dictionary audio_files, mapping a mood to a list of associated audio
"""
def download_all_audio(audio_dir = AUDIO_DIR):

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
def download_playlist(tag, video_id, max_downloads=None, audio_dir=AUDIO_DIR):
    print "Downloading playlist for [Tag:'{0}', Seed:'{1}]'\n".format(tag.upper(),video_id)

    #use seed_video to generate mix playlist id
    seed_video = pafy.new(video_id)
    playlist_id = seed_video.mix.plid    
    playlist = pafy.get_playlist(playlist_id)['items']
    
    #decide number of files to download
    if not max_downloads:
        max_downloads = len(playlist)
    download_count = min(len(playlist),max_downloads)
    wav_files = []
            
    #iterate over list of video urls to download their audio    
    for x in xrange(-1,download_count):
        if x == -1: 
            video = pafy.new(video_id) #process seed video
        else:
            video = playlist[x]['pafy'] #process playlist videos  
        
        #select stream with the best m4a audio
        stream = video.getbestaudio(preftype="m4a")
        title = re.sub(r'\W+', '', video.title.replace (" ", "_"))

        #initialize local audio file paths
        m4a_file = audio_dir + tag.upper() + "_" + title + "." + stream.extension
        wav_file = m4a_file[:-4] + '.wav'
        
        #if m4a doeasn't exist, download it
        print "Checking for previous download of {0}.m4a...".format(title)
        if not (os.path.isfile(m4a_file) or os.path.isfile(wav_file)):
            print "\tDownloading m4a ..."
            m4a_file = stream.download(filepath = m4a_file,quiet=True)
            print "\tDownload complete."
        
        #if wav doesn't exist, download it
        print "Checking for previous download of {0}.wav...".format(title) 
        if not os.path.isfile(wav_file):
            print "\tConverting m4a to wav ..."
            wav_file = convert_to_wav(m4a_file)
            print "\tConversion complete"

            #Delete the m4a file after conversion
            try: 
                print "\n\tDeleting original m4a file..."
                os.remove(m4a_file)
                print "\tDeletion of original m4a complete"
            except Exception as e:
                print str(e) + ": unable to remove m4a due to an unexpected exception..."
            
            
        wav_files.append(wav_file)
    
    print "Playlist download completed\n"
    return wav_files


"""
Relies on users' FFMPEG install to convert m4a to wav
User MUST have FFMPEG installed on their system path/system environ variables

!CAUTION!: If this is being run in an IDE, make sure the **IDE** has visibility
to system PATH variables in order to properly run FFMPEG.

Returns path to new wav file.
"""
def convert_to_wav(m4a_file,audio_dir = AUDIO_DIR):
    
    wav_file = m4a_file[:-4] + '.wav'
    
    m4a = AudioSegment.from_file(m4a_file)
    m4a.export(wav_file,format="wav")
    
    while not os.path.isfile(wav_file):
        time.sleep(1)
    
    return wav_file

def download_m4a(video_id,audio_dir=AUDIO_DIR):
    video = pafy.new(video_id)
    stream = video.getbestaudio(preftype="m4a")
    title = re.sub(r'\W+', '', video.title.replace (" ", "_"))

    m4a_file = audio_dir + "_" + title + "." + stream.extension
    m4a_file = stream.download(filepath = m4a_file)
        
    return m4a_file

def get_m4a(video_id, audio_dir = AUDIO_DIR):
    video = pafy.new(video_id)
    title = re.sub(r'\W+', '', video.title.replace (" ", "_"))
    m4a_file = audio_dir + "_" + title + ".m4a"

    #if file doesn't already exist, download it from stream
    if not (os.path.isfile(m4a_file)):
        stream = video.getbestaudio(preftype="m4a")
        m4a_file = stream.download(filepath = m4a_file)
    
    return m4a_file

def split_audio(music_file, audio_dir = AUDIO_DIR):
    print "Splitting '{}' into 3-minute chunks...".format(music_file)
    
    file_ext = music_file.split(".")[-1]
    audio = AudioSegment.from_file(music_file,format=file_ext)
   
    three_minutes = 3 * 60 * 1000
    chunk_size = min(three_minutes,len(audio))
    
    index = 0
    new_clips = []
    for i in xrange(0, len(audio), chunk_size):
        audio_chunk = audio[i:i+chunk_size]    
        new_clip = "{0}_{1}.wav".format(music_file[:-(len(file_ext)+1)],index)
        
        audio_chunk.export(new_clip)
        while not os.path.isfile(new_clip):
            time.sleep(1)
     
        new_clips.append(new_clip)        
        index+=1
    return new_clips
