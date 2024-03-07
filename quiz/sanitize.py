import re

def sanitize_artist(artist):
    artist = re.sub('[^0-9a-zA-Z]+', '', artist)
    if artist.lower() == "ghost":
        artist = "ghostbc"
    return artist

def sanitize_song(song):
    song = re.sub('[^0-9a-zA-Z]+', '', song)
    return song

def sanitize_lyrics(lyrics):
    # Clean data
    lyrics = lyrics.replace("\r"," ").replace("\n"," ")
    # lyrics = ''.join(filter(str.isalpha or str.whitespace, lyrics))
    lst = lyrics.split(" ",)
    for i in range(0,len(lst)):
        lst[i] = re.sub(r'[^a-zA-Z0-9_\']+', '', lst[i])
    # TODO: Clean up words like "Ooh" -> "Oh"

    lst = list(filter(lambda a: a != "", lst))
    return lst
