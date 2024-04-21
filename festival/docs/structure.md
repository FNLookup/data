# Documentation

## Structure for `festival_tracks.json`

- tracks
  - every item has the following structure
    - lastModified: 12345678.90
    - active: 12345678.90
    - language: en-US
    - id: song
    - title: Song
    - year: 2024
    - artist: FNLookup
    - album: Song Album
    - genres: []
    - scale: Major
    - gameplay_tags: [s294_sparktrack_123456]
    - item_id: something_sid_284969
    - preview_start: 7382.1395
    - instrument_defaults
      - vocals: Vocals
      - guitar: Guitar
      - drums: Drums
      - bass: Bass
    - difficulties
      - plastic_bass: 0
      - plastic_drums: 0
      - plastic_guitar: 0
      - vocals: 0
      - bass: 0
      - drums: 0
      - guitar: 0
    - duration: 0
    - album_image: url
    - bpm: 100
    - preview_start: 50
    - genre: music
    - key: Eb
    - resources: []
       - every item has the following structure
          - url: resource url
          - type: resource type
    - isrc: US12345678
    - rating: T
    - event_id: 1a2b3c-4d5e
    - join_code: 0000-1111-2222

## Descriptions

`tracks`
array with every track's details

`id`
short string with the song in lower case used for identifying the song in lists

`lastModified`
unix timestamp with the lastmodified time on this track

`active`
unix timestamp with the active time on this track

`language`
track specified language

`album`
song album

`title`
song title

`year`
release year

`artist`
song artist

`genres`
array of asigned genders

`gameplay_tags`
array containing general item tags

`preview_start`
specifies in seconds when the 30s long preview takes place in the original song

`item_id`
placeholder ids or ids to link with the owned jam tracks in thw locker

`scale`
music scale: major, minor

`instrument_defaults`
object containing the icons for each instrument, also represents the ingame instrument for that track

`instrument_defaults.vocals`
instrument used ingame for vocals track

`instrument_defaults.guitar`
instrument used ingame for guitar track

`instrument_defaults.drums`
instrument used ingame for drums track

`instrument_defaults.bass`
instrument used ingame for bass track

`difficulties`
object with the difficulty for every track

`difficulties.plastic_bass`
difficulty level for plastic bass

`difficulties.plastic_drums`
difficulty level for plastic drums

`difficulties.plastic_guitar`
difficulty level for plastic guitar

`difficulties.vocals`
difficulty level for vocals

`difficulties.bass`
difficulty level for bass

`difficulties.drums`
difficulty level for drums

`difficulties.guitar`
difficulty level for guitar

`duration`
duration in seconds

`album_image`
album art url

`bpm`
bpm for this track

`key`
music key for the track

`resources`
object containing resources that may be useful for devs

`resources[].url`
url or id for this resource

`resources[].type`
type of this resource

currently there are only four resources those being:
- lipsync .lad
- midi .dat
- qi.sid
- qi.pid

`isrc`
the isrc code for the song

`rating`
isrb rating for this song (E,T)

`event_id`
some id used by epic

`join_code`
creative codes i guess.