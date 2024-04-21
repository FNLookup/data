# Blurl obtaining
Steps to reach blurl for the streaming

## Step 1
Select a song from the Fortnite Content API list

Spark tracks page: `https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game/spark-tracks`

As an example I have selected:

```"dontfearthereaper":{"_title":"dontfearthereaper","track":{"tt":"(Don't Fear) The Reaper","nu":"2024-03-28T23:00:00.000Z","ry":1976,"dn":322,"sib":"Bass","sid":"Drum","sig":"Guitar","qi":"{\"sid\":\"aa4f6195-5070-42cc-afaf-55db3d61bba8\",\"pid\":\"3f7619fe-66b9-48d4-94a7-3f94189c4b67\",\"title\":\"dontfearthereaper\",\"tracks\":[{\"part\":\"ds\",\"channels\":[\"FL\",\"FR\"],\"vols\":[4,4]},{\"part\":\"bs\",\"channels\":[\"FL\",\"FR\"],\"vols\":[4,4]},{\"part\":\"gs\",\"channels\":[\"FL\",\"FR\"],\"vols\":[4,4]},{\"part\":\"vs\",\"channels\":[\"FL\",\"FR\"],\"vols\":[4,4]},{\"part\":\"fs\",\"channels\":[\"FL\",\"FR\"],\"vols\":[4,4]}],\"preview\":{\"starttime\":30.4018}}","sn":"dontfearthereaper","ge":["Rock"],"mk":"A","mm":"Minor","ab":"Agents of Fortune","siv":"Vocals","su":"75d14ea0-99b6-41a6-8c68-bca89bddded7","in":{"pb":2,"pd":5,"vl":2,"pg":4,"_type":"SparkTrackIntensities","gr":5,"ds":6,"ba":5},"mt":141,"_type":"SparkTrack","mu":"https://cdn2.unrealengine.com/w2ew41kecdgxucto-0a3c19befbf4.dat","an":"Blue Öyster Cult","gt":["Jam-LoopIsUnpitched-Beat"],"ar":"E","au":"https://cdn2.unrealengine.com/ctzomncwaembo4i9-512x512-4f2be6de1f0e.png","ti":"SparksSong:sid_placeholder_20","ld":"https://cdn2.unrealengine.com/dontfearthereaper-b6164b6c8410.lad","jc":"3969-4510-2918"},"_noIndex":false,"_activeDate":"2023-10-09T21:22:07.220Z","lastModified":"2024-03-19T15:20:54.542Z","_locale":"en-US","_templateName":"track"}```

Don't Fear The Reaper by Blue Oyster

## Step 2
Extract sid (Song Streaming ID) from qi (for Preview use pid)

`aa4f6195-5070-42cc-afaf-55db3d61bba8` is our Song Streaming ID

## Step 3
Join Streaming CDN URL with our Song Streaming ID

`https://cdn.qstv.on.epicgames.com/` is our Streaming CDN service

When joined by `aa4f6195-5070-42cc-afaf-55db3d61bba8` we are resulted with:

`https://cdn.qstv.on.epicgames.com/aa4f6195-5070-42cc-afaf-55db3d61bba8`

This URL does not require Auth.

## Step 4
### Obtaining Blurl (to obtain MPD directly skip to step 5)
Obtain Blurl URL

In the content returned by `https://cdn.qstv.on.epicgames.com/aa4f6195-5070-42cc-afaf-55db3d61bba8` we have a few values:

```{"playlist":"This is actually already the MPD just encoded in Base64 format","playlistType":"application/dash+xml","metadata":{"assetId":"","baseUrls":["https://fortnite-vod.akamaized.net/yZUGFgMbTQzURFyVgh/1706206034/","https://pilgrim.qstv.on.epicgames.com/yZUGFgMbTQzURFyVgh/1706206034/"],"supportsCaching":true,"version":"1706206034"}}```

`metadata.baseUrls` contains 2 URLs: 

- `https://fortnite-vod.akamaized.net/yZUGFgMbTQzURFyVgh/1706206034/`
- `https://pilgrim.qstv.on.epicgames.com/yZUGFgMbTQzURFyVgh/1706206034/`

(Note: the pilgrim.qstv.on.epicgames.com URL, although based entirely around festival, due to its codename being Pilgrim somewhere, isn't present in this Jam Track anymore. What I mean by this is just ignore it.)

Our interest is in the first URL as it does not require Auth, the other one is only used by the game client and requires Auth.

We can see `/1706206034/` is common across both.

On the first URL we see a structure

`https://fortnite-vod.akamaized.net/:VUIDPath/:UnknownID/`

To obtain a blurl we must not use the Unknown ID and instead replace it with `master.blurl`.

For our song, this would be:

`https://fortnite-vod.akamaized.net/yZUGFgMbTQzURFyVgh/master.blurl`

We have now obtained our blurl.

## Step 5
### Obtaining MPD directly

We can use the `playlist` value in the returned content by `https://cdn.qstv.on.epicgames.com/:sid` and decode it from base64 to get our MPD content directly, or...

using our previously declared structure (`https://fortnite-vod.akamaized.net/:VUIDPath/:UnknownID/`) we join `main.mpd` to our URL.

For our song this would be:

`https://fortnite-vod.akamaized.net/yZUGFgMbTQzURFyVgh/1706206034/main.mpd`

We have obtained our MPEG-Dash playlist.
However, we may not be able to decrypt it without the blurl.