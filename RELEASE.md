# Release notes

## 0.3.6

- Removed duplicate project name (see [#95](https://github.com/GioF71/subsonic-connector/issues/95))
- Add RELEASE.md

## 0.3.5

- Using getStarred2
- Improved linting (still sucks though)

## 0.3.4

- Bump py-sonic to 1.0.1

## 0.3.3

- Corrected py-sonic dependency in pyproject.toml

## 0.3.2

- Album: Corrected getOriginalReleaseDate
- Album: Add getOriginalReleaseYear
- Album: Add getOriginalYearWithYear
- launch.json updated with "debugpy" instead of "python"
- Item: linting improved
- Updated tests

## 0.3.1

- Bump to 0.3.1
- Add support for originalReleaseDate
- Also fixed some linting

## 0.3.0

- Support multiple genres
- Allow access to item (avoids need for breaking changes)

## 0.2.6

- allow format and max_bitrate when creating url

## 0.2.5

- Avoid to add format to stream url

## 0.2.4

- Support for legacy authentication

## 0.2.3

- Search uses search2 underlying method (id3)
- Corrections in tests (handle possible failures)

## 0.2.2

- Improve getCoverByArtist
- Add test for highest rated albums

## 0.2.1

- Prefer id3 variants
- use getArtistInfo2 instead of getArtistInfo
- use getSimilarSongs2 instead of getSimilarSongs
- misc bug fixes

## 0.2.0

- Prefer id3 variants
- use getArtistInfo2 instead of getArtistInfo
- use getSimilarSongs2 instead of getSimilarSongs
- misc bug fixes

## 0.1.17

- Add support for getStarred

## 0.1.16

- similar songs (#75)
- minor change in getCoverByArtist
- back to be compatibile with python 3.9
- Similar Songs implemented

## 0.1.15

- Support for top songs
- support for artist_info

## 0.1.14

- Support Radios #70 (#71)

## 0.1.13

- Scrobble support #66 (#67)
- Add getCoverArt to ArtistListItem #64 (#65)

## 0.1.11

- Support playlists #60 (#61)
- Add ping method #58 (#59)
- Update README.md (#57)

## 0.1.10

- py-sonic version bump #53 (#54)

## 0.1.9

- Album class is missing some info #49 (#50)

## 0.1.8

- Add support for download #45 (#46)
- Add method isOk on Response #43 (#44)

## 0.1.7

- Add format to stream URL #39 (#40)

## 0.1.6

- Separate method for auth arguments in url creation #35 (#36)
- Add 'getSong' method #32 (#34)
- Enum for ltype #29 (#31)
- Generic class for responses #28 (#30)
- Interface for configuration #26 (#27)

## 0.1.5

- Add getSongCount() in Album #23 (#24)

## 0.1.4

- Create Response from dict #20 (#21)
- Reduce number of classes extending Item #18 (#19)
- Documentation: Add build information #16 (#17)

## 0.1.3

- Add getalbum method (#15)
- Add 'getAlbum' method #14
- Add support for getAlbum (take 2)
- Documentation: Add reference to pysonic library #10 (#11)

## 0.1.1

- Initial release
