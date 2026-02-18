#!/usr/bin/env python

import urllib
import libsonic
from dotenv import dotenv_values
from pprint import pprint
import os

# basic parameters
base_url: str = os.getenv("SUBSONIC_SERVER_URL")
port: int = int(os.getenv("SUBSONIC_SERVER_PORT"))
username: str = os.getenv("SUBSONIC_USERNAME")
password: str = os.getenv("SUBSONIC_PASSWORD")
legacy_auth: bool = os.getenv("SUBSONIC_LEGACY_AUTH", "false").lower() == "true"

# load custom headers. They are loaded correctly
custom_headers: dict[str, str] = {}
custom_headers_file_name = os.getenv("SUBSONIC_CUSTOM_HEADERS_FILE_NAME")
# print(f"custom_headers_file_name [{custom_headers_file_name}]")
if custom_headers_file_name:
    custom_headers.update(dotenv_values(custom_headers_file_name))
    custom_headers["User-Agent"] = "upmpdcli"
    # print(f"custom_headers [{custom_headers}]")

custom_headers_tuple: list[tuple[str, str]] = [
    ("CF-Access-Client-Id", custom_headers["CF-Access-Client-Id"]),
    ("CF-Access-Client-Secret", custom_headers["CF-Access-Client-Secret"]),
    ("User-Agent", custom_headers["User-Agent"])
    ]

# first try!
# Initialize the connection using new constructor argument customHeaders
raw_conn = libsonic.Connection(
    baseUrl=base_url,
    # baseUrl='http://127.0.0.1',
    port=port,
    # port=8000,
    username=username,
    password=password,
    legacyAuth=legacy_auth,
    customHeaders=custom_headers)

# Create a custom opener that injects the headers for EVERY request
opener = urllib.request.build_opener()
opener.addheaders = [
    ('CF-Access-Client-Id', custom_headers["CF-Access-Client-Id"]),
    ('CF-Access-Client-Secret', custom_headers["CF-Access-Client-Secret"]),
    ("User-Agent", custom_headers["User-Agent"])
    ]
# force custom opener in raw_conn
raw_conn._opener = opener

# Now try the request
songs = raw_conn.getRandomSongs(size=2)
# works!
print(songs)

# second try
# will not force the custom opener -> http error 403
conn = libsonic.Connection(
    baseUrl=base_url,
    # baseUrl='http://127.0.0.1',
    port=port,
    # port=8001,
    username=username,
    password=password,
    legacyAuth=legacy_auth,
    customHeaders=custom_headers
)
# Let's get 2 completely random songs
songs = conn.getRandomSongs(size=2)

for song in songs['randomSongs']['song']:
    song_id = song['id']
    reloaded_song = conn.getSong(song_id)
    pprint(reloaded_song)
# We'll just pretty print the results we got to the terminal
pprint(songs)

i: int
for i in range(1000):
    env_k: str = f"ALBUM_QUERY_{i}"
    env_v: str = os.getenv(env_k)
    if not env_v:
        break
    print(f"Album query: [{env_v}]")
    search_result = conn.search3(query=env_v)
    if 'searchResult3' not in search_result:
        continue
    if 'album' not in search_result['searchResult3']:
        continue
    albums = search_result['searchResult3']['album']
    for album in albums:
        pprint(album)
