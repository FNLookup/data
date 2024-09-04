import json
import requests
from datetime import datetime
import time
import os

def transform_data(input_data, output_file):
    transformed_data = {"tracks": [], "lastModified": 0}

    wbhk = os.getenv('WKFL')

    for track_id, track_data in input_data.items():
        if track_id == "lastModified":
            unix_timestamp = datetime.strptime(track_data, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()
            transformed_data["lastModified"] = unix_timestamp

        if not isinstance(track_data, dict):
            continue

        transformed_track = {}

        transformed_track['lastModified'] = datetime.strptime(track_data["lastModified"], "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()
        transformed_track['active'] = datetime.strptime(track_data["_activeDate"], "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()
        transformed_track['language'] = track_data.get("_locale", 'LOLCAT')
        track_info = track_data['track']

        transformed_track['id'] = track_id
        transformed_track['title'] = track_info.get('tt', 'FNLOOKUP_NOTITLE')
        transformed_track['artist'] = track_info.get('an', 'FNLOOKUP_NOARTIST')
        transformed_track['album'] = track_info.get('ab', "")
        transformed_track['genres'] = track_info.get('ge', [])
        transformed_track['year'] = track_info.get('ry', 2000)
        transformed_track['duration'] = track_info.get('dn', 0)
        transformed_track['instrument_defaults'] = {
            'vocals': track_info.get('siv', ""),
            'bass': track_info.get('sib', ""),
            'drums': track_info.get('sid', ""),
            'guitar': track_info.get('sig', "")
        }
        transformed_track['gameplay_tags'] = track_info.get('gt', [])
        transformed_track['join_code'] = track_info.get('jc', "")
        transformed_track['item_id'] = track_info.get('ti', "")
        transformed_track['difficulties'] = {
            'plastic_bass': track_info['in'].get('pb', 0),
            'plastic_drums': track_info['in'].get('pd', 0),
            'plastic_guitar': track_info['in'].get('pg', 0),
            'vocals': track_info['in'].get('vl', 0),
            'guitar': track_info['in'].get('gr', 0),
            'drums': track_info['in'].get('ds', 0),
            'bass': track_info['in'].get('ba', 0)
        }
        transformed_track['scale'] = track_info.get('mm', 'Minor')
        transformed_track['album_image'] = track_info.get('au', '')        
        transformed_track['bpm'] = track_info.get('mt', 120)
        transformed_track['key'] = track_info.get('mk', 'A')
        transformed_track['event_id'] = track_info.get('su', None)
        transformed_track['isrc'] = track_info.get('isrc', "")
        transformed_track['rating'] = track_info.get('ar', "") # ESRB

        track_qi = json.loads(track_info.get("qi", '{"ph": 0, "lol": "epic why"}'))

        transformed_track['preview_start'] = track_qi.get('preview').get("starttime", 123456)

        transformed_track['resources'] = [
            {
                'url': track_info.get('mu', ''),
                'type': 'Sparks_Encrypted_Midi'
            },
            {
                'url': track_info.get('ld', ""),
                'type': 'Sparks_Lip_Sync'
            },
            {
                'url': track_qi.get('sid', ''),
                'type': 'Pilgrim_Streaming_ID_Song'
            },
            {
                'url': track_qi.get('pid', ''),
                'type': 'Pilgrim_Streaming_ID_Prev'
            }
        ]

        transformed_data["tracks"].append(transformed_track)

    ogstuff = open(output_file, 'r').read()

    with open(output_file, 'w') as f:
        alltransform = json.dumps(transformed_data, indent=4)
        f.write(alltransform)

        try:
            if ogstuff != alltransform:
                # new jam tracks
                set_old = json.loads(ogstuff)['tracks']
                newjt = [item for item in json.loads(alltransform)['tracks'] if item not in set_old]
                strnewjtrs = 'New/Updated Jam Tracks:\n'
                for t in newjt:
                    strnewjtrs += t['artist'] + ' - ' + t['title'] + '\n'
                message = {
                    "content": os.getenv("UTP") + " **JAM TRACKS UPDATED:** \n" + strnewjtrs
                }
                print('NEW JAM TRACKS!')
                requests.post(wbhk, json=message)
        except Exception as e:
            print(f"Exception lol:{e}")

if __name__ == "__main__":
    api_url = "https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game/spark-tracks"
    print("Receiving data from", api_url)
    response = requests.get(api_url)
    if response.status_code == 200:
        print("Data received. Converting...")
        input_data = response.json()
        output_file = "festival/jam_tracks.json"
        output_original = "festival/spark-tracks.json"
        transform_data(input_data, output_file)
        print("Data transformation complete. Transformed data saved to", output_file)
        with open(output_original, 'w') as f:
            json.dump(input_data, f, indent=4)
            print("Original Saved")
    else:
        print("Failed to fetch data from Fortnite Content: Status code ", response.status_code)
