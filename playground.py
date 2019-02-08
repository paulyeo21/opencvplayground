# global imports
import numpy
import cv2
import subprocess

# local imports
import twitch_api

# Get tfue vods
def getTfueVods():
    users = twitch_api.getUsersByLoginNames("tfue")
    tfue = [user for user in users if user["name"] == "tfue"][0]
    tfue_vods = twitch_api.getChannelVods(tfue["_id"])
    return tfue_vods

tfue_vods = getTfueVods()
print(tfue_vods[2])

# Use ffmpeg and youtube-dl to open vod 
# youtube_dl_cmd = [ "youtube-dl", "-f", "best", tfue_vods[0]["url"] ]
# command = [ "ffmpeg", "-i", tfue_vods[0]["url"], "-f", "image2pipe", "-pix_fmt", "rgb24", "-vcodec", "rawvideo", "-" ]

# Pipe output to python to read vod frame by frame *bufsize must be > one frame
# pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)

# Get frame
# image = numpy.fromstring(pipe.stdout.read(420*360*3), dtype="uint8")

# shape as a numpy array
# image = image.reshape((360, 420, 3))

# cap = cv2.VideoCapture("https://www.twitch.tv/videos/375747829")
# print(cap)
