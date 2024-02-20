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
    else:
        album = "N/A"
        song = "N/A"
    return render_template("quiz.jinja", title="Fill In The Blank", band=band, album=album, song=song, lyrics=song_lyrics)