# https://fortnitecentral.genxgames.gg/api/v1/mappings
# https://fortnitecentral.genxgames.gg/api/v1/aes
# https://fortnitecentral.genxgames.gg/api/v1/hotfixes?lang=en

import requests
import json
import time

def fetch_save(url):
    print("Attempting to fetch", url)
    
    response = requests.get(url)
    if response.status_code == 200:
        print("Fetch successful")
        return response.json()
    else:
        print(f"Failed to fetch FNCentral API: {response.status_code}")
        print("Response content:", response.content)
        return None
    
to_fetch = [{
    "url": "https://fortnitecentral.genxgames.gg/api/v1/mappings",
    "path": "mappings.json"
},{
    "url": "https://fortnitecentral.genxgames.gg/api/v1/aes",
    "path": "aes.json"
},{
    "url": "https://fortnitecentral.genxgames.gg/api/v1/hotfixes?lang=en",
    "path": "hotfixes_en.json"
}]

for dir in to_fetch:
    data = fetch_save(dir["url"])
    with open("fncentral/" + dir["path"], "w") as file:
        json.dump(data, file, indent=4)
        print("Data saved to file")