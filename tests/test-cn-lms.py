#!/usr/bin/env python

from pprint import pprint
import libsonic
import os

base_url : str = os.getenv("SUBSONIC_SERVER_URL")
port : int = int(os.getenv("SUBSONIC_SERVER_PORT", "5082"))
username : str = os.getenv("SUBSONIC_USERNAME")
password : str = os.getenv("SUBSONIC_PASSWORD")
legacy_auth : bool = os.getenv("SUBSONIC_LEGACYAUTH", "true").lower() == "true"

# We pass in the base url, the username, password, and port number
# Be sure to use https:// if this is an ssl connection!
conn = libsonic.Connection(
    baseUrl = base_url,
    port = port,
    username = username,
    password = password,
    legacyAuth = legacy_auth,
)
# Let's get 2 completely random songs
songs = conn.getRandomSongs(size=2)

for song in songs['randomSongs']['song']:
    song_id = song['id']
    reloaded_song = conn.getSong(song_id)
    pprint(reloaded_song)
# We'll just pretty print the results we got to the terminal
pprint(songs)
