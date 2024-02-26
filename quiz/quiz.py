import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from azlyrics.azlyrics import artists, songs, lyrics
import json
import random

bp = Blueprint('quiz', __name__, url_prefix='/quiz')

@bp.route("/start", methods={'POST'})
def quiz():
    band = request.form['search']
    print(band[0])

    artists_by_letter= json.loads(artists(band[0]))
    is_band = band in artists_by_letter
    print(is_band)

    if is_band:
        songs_by_album = json.loads(songs(band))
        
        album = random.choice(list(songs_by_album['albums']))
        song = random.choice(songs_by_album['albums'][album])

        song_lyrics_arr = lyrics(band, song)
        song_lyrics = song_lyrics_arr[0]
        song_lyrics_lst = sanitize_lyrics(song_lyrics)
        song_lyrics_lst = organize_lyrics(song_lyrics_lst)
    else:
        album = "N/A"
        song = "N/A"
    return render_template("quiz.jinja", title="Fill In The Blank", band=band, album=album, song=song, lyrics=song_lyrics, lyrics_lst=song_lyrics_lst)

def sanitize_lyrics(lyrics):
    # Clean data
    lyrics = lyrics.replace("\r"," ").replace("\n"," ")
    # lyrics = ''.join(filter(str.isalpha or str.whitespace, lyrics))
    lst = lyrics.split(" ",)
    lst = list(filter(lambda a: a != "", lst))
    # TODO: Find a way to get rid of all punctuation. Except for apostrophes?.
    # TODO: Clean up words like "Ooh" -> "Oh"

    print(lst)
    return lst

def organize_lyrics(lyrics_arr):
    lyrics_arr = lyrics_arr
    col_len = 50
    table = []
    col = []

    while lyrics_arr != []:
        # TODO: Adjust indices, likely off by 1.
        col = lyrics_arr[:50]
        lyrics_arr = lyrics_arr[50:]
        table.append(col)

    return table
