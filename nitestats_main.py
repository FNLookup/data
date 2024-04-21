import requests
import json
import time
import os

def fetch_save(url):
    print("Attempting to fetch", url)
    
    response = requests.get(url)
    if response.status_code == 200:
        print("Fetch successful")
        return response.json()
    else:
        print(f"Failed to fetch NiteStats API: {response.status_code}")
        print("Response content:", response.content)
        return None
    
to_fetch = [{
    "url": "https://api.nitestats.com/v1/epic/modes-smart",
    "path": "event_flags.json"
},{
    "url": "https://api.nitestats.com/v1/epic/store",
    "path": "store_front.json"
},{
    "url": "https://api.nitestats.com/v1/epic/lightswitch",
    "path": "light_switch.json"
}]

for dir in to_fetch:
    data = fetch_save(dir["url"])
    directory = "nitestats"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open("nitestats/" + dir["path"], "w") as file:
        json.dump(data, file, indent=4)
        print("Data saved to file")
    with open("nitestats/timestamp.json", "w") as file:
        file.write('{"timestamp": ' + str(time.time()) + '}')
        print("Timestamp saved to file")