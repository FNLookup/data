# Stems

#### Warning 
These are often encrypted and are not meant for you to have. Go your own way!

## Steps

- Get BLURL and MPD data. Refer to this guide [here](https://github.com/FNLookup/data/blob/main/festival/docs/blurl.md)

- Get encryption key.
    
    This is obtainable from the BLURLs `ev` value, or Envelope.
- Download segments.

    - The ammount of segments to be downloaded can be obtained by dividing the duration of the playlist by the segment duration. Both of these values are present on the MPD itself.

    - Pick a representation and parse its pattern.

    - Download init file, usually `init_adaptation.mp4`

    - Download each segment, usually the URL without `main.mpd` and instead `segment_adaptation_id.m4s`

    - Merge to a master file.

- Decrypt this file.

    - Preferibly use ffmpeg.
        
        Command: `ffmpeg -decryption_key key -i file.mp4 -c copy file_decrypt.mp4`
    
    The 10 track opus file can be opened in Audacity, with FFmpeg for Audacity installed.