import requests

TWITCH_CLIENT_ID = "9kfqeprglyqhxn3kmopdg8stbq8lje"

# input: "dallas,dallasnchains"
# output:
# [
#     {
#         "_id": "44322889",
#         "bio": "Just a gamer playing games and chatting. :)",
#         "created_at": "2013-06-03T19:12:02.580593Z",
#         "display_name": "dallas",
#         "logo": "https://static-cdn.jtvnw.net/jtv_user_pictures/dallas-profile_image-1a2c906ee2c35f12-300x300.png",
#         "name": "dallas",
#         "type": "staff",
#         "updated_at": "2017-02-09T16:32:06.784398Z"
#     },
#     {
#         "_id": "129454141",
#         "bio": null,
#         "created_at": "2016-07-13T14:40:42.398257Z",
#         "display_name": "dallasnchains",
#         "logo": null,
#         "name": "dallasnchains",
#         "type": "user",
#         "updated_at": "2017-02-04T14:32:38.626459Z"
#     }
# ]

def getUsersByLoginNames(logins):
    headers = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": TWITCH_CLIENT_ID
    }
    response = requests.get(f"https://api.twitch.tv/kraken/users?login={logins}", headers=headers)
    if not response.status_code > 400:
        return response.json()["users"]

# input: "60056333"
# output:
# [
#     {
#         "_id": "v102381501",
#         "broadcast_id": 23711574096,
#         "broadcast_type": "highlight",
#         "channel": {
#             "_id": "20694610",
#             "display_name": "Towelliee",
#             "name": "towelliee"
#         },
#         "created_at": "2016-11-20T23:46:06Z",
#         "description": "Last minutes of stream",
#         "description_html": "Last minutes of stream<br>",
#         "fps": {
#             "chunked": 59.9997939597903,
#             "high": 30.2491085172346,
#             "low": 30.249192959941,
#             "medium": 30.2491085172346,
#             "mobile": 30.249192959941
#         },
#         "game": "World of Warcraft",
#         "language": "en",
#         "length": 201,
#         "preview": {
#             "large": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-640x360.jpg",
#             "medium": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-320x180.jpg",
#             "small": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-80x45.jpg",
#             "template": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-{width}x{height}.jpg"
#         },
#         "published_at": "2016-11-20T23:46:06Z",
#         "resolutions": {
#             "chunked": "1920x1080",
#             "high": "1280x720",
#             "low": "640x360",
#             "medium": "852x480",
#             "mobile": "400x226"
#         },
#         "status": "recorded",
#         "tag_list": "",
#         "thumbnails": {
#             "large": [{
#                 "type": "generated",
#                 "url": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-640x360.jpg"
#             }],
#             "medium": [{
#                 "type": "generated",
#                 "url": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-320x180.jpg"
#             }],
#             "small": [{
#                 "type": "generated",
#                 "url": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-80x45.jpg"
#             }],
#             "template": [{
#                 "type": "generated",
#                 "url": "https://static-cdn.jtvnw.net/s3_vods/664fa5856b_towelliee_23711574096_550644271//thumb/thumb102381501-{width}x{height}.jpg"
#             }]
#         },
#         "title": "Last minutes of stream",
#         "url": "https://www.twitch.tv/towelliee/v/102381501",
#         "viewable": "public",
#         "viewable_at": null,
#         "views": 1761
#     }
# ]
def getChannelVods(user_id):
    headers = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": TWITCH_CLIENT_ID
    }
    response = requests.get(f"https://api.twitch.tv/kraken/channels/{user_id}/videos", headers=headers)
    if not response.status_code > 400:
        return response.json()["videos"]

def getVideo(video_id):
    headers = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": TWITCH_CLIENT_ID
    }
    response = requests.get(f"https://api.twitch.tv/kraken/videos/{video_id}", headers=headers)
    if not response.status_code > 400:
        return response.json()


if __name__ == "__main__":
    users = getUsersByLoginNames("tfue")
    tfue = [user for user in users if user["name"] == "tfue"][0]
    tfue_vods = getChannelVods(tfue["_id"])
    video = getVideo(tfue_vods[0]["_id"])
    print(video)

