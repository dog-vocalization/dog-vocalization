from __future__ import print_function
from pychromecast.controllers.youtube import YouTubeController

import pychromecast
import time

print(pychromecast.get_chromecasts_as_dict().keys())

# set up the chrome cast with its name
cast = pychromecast.get_chromecast(friendly_name="GeneralUse")

cast.wait()

mc = cast.media_controller

# yt = YouTubeController()
#
# cast.register_handler(yt)
#
# #yc = cast.youtube_controller
#
# yt.play_video('tgIqecROs5M')

# default
mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')

#time.sleep(5)

#mc.play_media('http://localhost:8000/Sail.mp4', 'video/mp4')

# mc.stop() to stop
# mc.play() to resume