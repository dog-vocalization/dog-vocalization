import pafy
import os

##This link might be helpful later on:
#https://www.researchgate.net/post/How_can_I_compare_the_frequency_spectra_of_two_different_audio_signals

##Audio libraries??
#pyaudio
#chromaprint
#audioread

##Pafy Documentation
#https://pythonhosted.org/pafy/


#########################################################
#Get user input for playlist and playlist download dir

#example playlist_id = "PL358C088ACE11696A"
print "\
<<< YOUTUBE PLAYLIST AUDIO DOWNLOADER >>>\n\
WARNING: There are no checks to ensure that any user-entered\n\
    data such as playlist id or music folder are valid.\n\
    Proceed at your own risk.\n"

user_music_folder = raw_input("Target music folder: ")

isMix = raw_input("Video url to generate yt mix playlist. \n\
    (if blank, you will be prompted for a playlist id instead): ")
if not isMix:
    user_playlist_id = raw_input("Target playlist id: ")

else:
    video = pafy.new(isMix)
    user_playlist_id = video.mix.plid
    

#########################################################
#set current working directory, the save folder for music
path = user_music_folder

#if user defined path doesn't exist, create it
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise

#change working directory to user-desired directory
os.chdir(path)
print os.getcwd()


#########################################################
#Main Loop.  Initialize playlist, then start downloads

playlist_and_meta = pafy.get_playlist(user_playlist_id)
#note, look into api "playlist2" to get larger results

playlist = playlist_and_meta['items']
playlist_length = len(playlist)

for x in xrange(playlist_length):
    video = playlist[x]['pafy']
    print video.videoid
    stream = video.getbestaudio()
    fname = stream.download("")

print "done processing playlist"
