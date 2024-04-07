import functools
from flask import (
    abort, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .sanitize import sanitize_artist, sanitize_song, sanitize_lyrics

from azlyrics.azlyrics import artists, songs, lyrics
import json
import math
import random
import re

bp = Blueprint('quiz', __name__, url_prefix='/')

recent_songs = []
max_number_of_recent_songs = 5

@bp.route("/start", methods={'POST'})
def quiz():
    band = request.form['search']
    print("Searching for band:", band)

    artists_by_letter= json.loads(artists(band[0]))
    print("Artists By Letter: ", artists_by_letter)
    is_band = False
    sanitized_band = ''
    for artist in artists_by_letter:
        if band.lower() == artist.lower():
            print("Found band %s on AZLyrics." % (band))
            is_band = True
            sanitized_band = sanitize_artist(band)
    print("Pre-Sanitized Band name:", band)
    print("Sanitized Band name:", sanitized_band)

    if is_band:
        print("Searching for all songs.")
        songs_by_album = json.loads(songs(sanitized_band))
        
        album = random.choice(list(songs_by_album['albums']))
        print("Random Album:", album)

        get_new_song = True
        while (get_new_song):
            song = random.choice(songs_by_album['albums'][album])
            print("Potential Song", song)
            print(recent_songs)
            if song not in recent_songs:
                get_new_song = False
                if len(recent_songs) >= max_number_of_recent_songs:
                    recent_songs.pop(0)
                recent_songs.append(song)


        print("Random Song:", song)



        sanitized_song = sanitize_song(song)

        song_lyrics_arr = lyrics(sanitized_band, sanitized_song)
        if type(song_lyrics_arr) == dict and 'Error' in song_lyrics_arr:
            print("Error", song_lyrics_arr)
            abort(404, description=song_lyrics_arr['Error'])
        song_lyrics = song_lyrics_arr[0]
        print("Retrieved song lyrics")
        song_lyrics_lst = sanitize_lyrics(song_lyrics)
        print("Sanitized song lyrics.")
        organized_lyrics = organize_lyrics(song_lyrics_lst)
        print("Organized song lyrics.")
    else:
        print("Did not find Band %s on AZLyrics." % (sanitized_band))
        abort(404,description="Artist " + sanitized_band + " was not found.")
    return render_template("quiz.jinja", title="Fill In The Blank", page="Lyrics Quiz", band_azlyrics=sanitized_band, band_search=band, album=album, song=song, lyrics=song_lyrics, lyrics_lst=organized_lyrics, total_lyrics=len(song_lyrics_lst))

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
