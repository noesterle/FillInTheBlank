import re

def sanitize_artist(artist):
    artist = re.sub('[^0-9a-zA-Z]+', '', artist)
    if artist.lower() == "ghost":
        artist = "ghostbc"
    return artist