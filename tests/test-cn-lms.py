#!/usr/bin/env python

from pprint import pprint
import libsonic

# We pass in the base url, the username, password, and port number
# Be sure to use https:// if this is an ssl connection!
conn = libsonic.Connection(
    baseUrl="http://192.168.1.174",
    port=5082,
    username="giovanni",
    password="HEn%CWgnRdfz5iAt2$495zcE",
    legacyAuth=True,
)
# Let's get 2 completely random songs
songs = conn.getRandomSongs(size=2)

for song in songs['randomSongs']['song']:
    song_id = song['id']
    reloaded_song = conn.getSong(song_id)
    pprint(reloaded_song)
# We'll just pretty print the results we got to the terminal
#pprint(songs)
