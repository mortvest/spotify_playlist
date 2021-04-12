import json
import re
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise ValueError("Please provide a playlist url")
    url = sys.argv[1]

    try:
        r = requests.get(url)
        lines = r.text.split("\n")
        playlist_json = json.loads(re.findall("Spotify\.Entity = (\{.*\})", r.text, re.MULTILINE)[0])
        items = playlist_json["tracks"]["items"]
    except:
        raise ValueError("Could not read the playlist from url. Please provide a url to a valid Spotify playlist")

    for item in items:
        track_dict = item["track"]
        # album_name = track_dict["album"]["name"]
        artist_name = track_dict["artists"][0]["name"]
        track_name = track_dict["name"]
        print("{} - {}".format(artist_name, track_name))
