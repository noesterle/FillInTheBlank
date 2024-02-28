import functools
from flask import (
    abort, Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from azlyrics.azlyrics import artists, songs, lyrics
import json
import math
import random
import re

bp = Blueprint('quiz', __name__, url_prefix='/')

@bp.route("/start", methods={'POST'})
def quiz():
    band = request.form['search']

    artists_by_letter= json.loads(artists(band[0]))
    is_band = band in artists_by_letter

    if is_band:
        songs_by_album = json.loads(songs(band))
        
        album = random.choice(list(songs_by_album['albums']))
        song = random.choice(songs_by_album['albums'][album])

        song_lyrics_arr = lyrics(band, song)
        if type(song_lyrics_arr) == dict and 'Error' in song_lyrics_arr:
            abort(404, description=song_lyrics_arr['Error'])
        song_lyrics = song_lyrics_arr[0]
        song_lyrics_lst = sanitize_lyrics(song_lyrics)
        organized_lyrics = organize_lyrics(song_lyrics_lst)
    else:
        album = "N/A"
        song = "N/A"
    return render_template("quiz.jinja", title="Fill In The Blank", band=band, album=album, song=song, lyrics=song_lyrics, lyrics_lst=organized_lyrics, total_lyrics=len(song_lyrics_lst))

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

def organize_lyrics(lyrics_arr):
    lyrics_arr = lyrics_arr
    col_len = 50
    table = []

    for i in range(0,col_len):
        table.append([])

    row_num = 0
    for lyric in lyrics_arr:
        table[row_num].append(lyric)
        row_num = (row_num + 1) % col_len

    return table
