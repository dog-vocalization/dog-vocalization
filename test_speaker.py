from __future__ import print_function
from pychromecast.controllers.youtube import YouTubeController

import pychromecast
import time

print(pychromecast.get_chromecasts_as_dict().keys())

# set up the chrome cast with its name
cast = pychromecast.get_chromecast(friendly_name="GeneralUse")

mc = cast.media_controller

# default
# mp3, m4a, mp4
#mc.play_media('https://www.prism.gatech.edu/~swatanabe8/Sail.mp4', 'video/mp4')
#mc.play_media('https://www.prism.gatech.edu/~swatanabe8/Sail.mp3', 'audio/mp3')
mc.play_media('https://www.prism.gatech.edu/~swatanabe8/Sail.m4a', 'audio/mp4')

#time.sleep(5)

# mc.stop() to stop
# mc.play() to resume