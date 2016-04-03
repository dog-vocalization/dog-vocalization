from __future__ import print_function
import pychromecast

print(pychromecast.get_chromecasts_as_dict().keys())

# set up the chrome cast with its name
cast = pychromecast.get_chromecast(friendly_name="GeneralUse")

cast.wait()

mc = cast.media_controller

mc.play_media()

# mc.stop() to stop
# mc.play() to resume