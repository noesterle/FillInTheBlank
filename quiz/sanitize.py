def sanitize_artist(artist):
    if artist.lower() == "ghost":
        artist = "ghostbc"
    return artist