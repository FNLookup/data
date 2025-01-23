## Jam Track Field Name Explanations

Each Track is a object in the root object, each `track` object has the following structure.

| Property             | Type     | Explanation                     |
| -------------------- | -------- | ------------------------------- |
| tt                   | string   | Track Title                     |
| ry                   | int      | Release Year                    |
| dn                   | int      | Duration (in seconds)           |
| sib                  | string   | Starting Instrument Bass        |
| sid                  | string   | Starting Instrument Drums       |
| sig                  | string   | Starting Instrument Guitar      |
| qi                   | string   | Quicksilver Data                |
| qi.sid               | string   | Song streaming UUID             |
| qi.pid               | string   | Preview streaming UUID          |
| qi.stereoId          | string   | Stereo streaming UUID           |
| qi.instrumentalId    | string   | Instrumental streaming UUID     |
| qi.title             | string   | Short song title                |
| qi.tracks            | object[] | Track Data                      |
| qi.preview           | object   | Preview Data                    |
| qi.preview.starttime | float    | Preview start time (in seconds) |
| sn                   | string   | Track Name for API              |
| ge                   | string[] | Song Genre                      |
| mk                   | string   | Key                             |
| mm                   | string   | Scale                           |
| ab                   | string   | Album Name                      |
| siv                  | string   | Starting Instrument Vocals      |
| su                   | string   | Event UUID                      |
| in                   | object   | Song Difficulties               |
| in.pb                | int      | Plastic Bass Difficulty         |
| in.pd                | int      | Plastic Drums Difficulty        |
| in.pg                | int      | Plastic Guitar Difficulty       |
| in.vl                | int      | Vocals Difficulty               |
| in.gr                | int      | Guitar Difficulty               |
| in.ds                | int      | Drums Difficulty                |
| in.ba                | int      | Bass Difficulty                 |
| mt                   | int      | BPM/Tempo                       |
| mu                   | string   | Encrypted MIDI Data URL         |
| an                   | string   | Artist Name                     |
| gt                   | string[] | Gameplay Tags                   |
| isrc                 | string   | ISR Code (ISRC)                 |
| ar                   | string   | ISRB Rating                     |
| au                   | string   | Album Art URL                   |
| ti                   | string   | Template ID                     |
| ld                   | string   | Lipsync Data URL                |
| jc                   | string   | Jam Link Code                   |

[Source](https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation/blob/main/EpicGames/FN-Content/Explanations/SparkTracks.md)
