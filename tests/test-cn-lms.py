#!/usr/bin/env python

from pprint import pprint
import libsonic
import os

base_url : str = os.getenv("SUBSONIC_SERVER_URL")
port : int = int(os.getenv("SUBSONIC_SERVER_PORT"))
username : str = os.getenv("SUBSONIC_USERNAME")
password : str = os.getenv("SUBSONIC_PASSWORD")
legacy_auth : bool = os.getenv("SUBSONIC_LEGACYAUTH", "false").lower() == "true"

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
#pprint(songs)

i : int
for i in range(1000):
    env_k : str = f"ALBUM_QUERY_{i}"
    env_v : str = os.getenv(env_k)
    if not env_v: break
    print(f"Album query: [{env_v}]")
    search_result = conn.search3(query = env_v) 
    if not 'searchResult3' in search_result: continue
    if not 'album' in search_result['searchResult3']: continue
    albums = search_result['searchResult3']['album']
    for album in albums:
        pprint(album)
