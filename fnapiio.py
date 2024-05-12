import requests
import json
import time
import os

def fetch_save(url):
    print("Attempting to fetch", url)

    headers = {
        "Authorization": os.getenv('API_KEY')
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Fetch successful")
        return response.json()
    else:
        print(f"Failed to fetch Fortnite API: {response.status_code}")
        print("Response content:", response.content)
        return None

language_list = ['en', 'ar', 'de', 'es', 'es-419', 'fr', 'it', 'ja', 'ko', 'pl', 'pt-BR', 'ru', 'tr', 'zh-CN', 'zh-Hant']
to_fetch = [{
    "url": "https://fortniteapi.io/v2/items/list?fields=images,displayAssets,name,id,gameplayTags,rarity,type,series",
    "path": "items_all"
},{
    "url": "https://fortniteapi.io/v2/items/list?fields=images,name,id,type,shopHistory",
    "path": "items_smaller"
}]

for lang in language_list:
    for dir in to_fetch:
        data = fetch_save(dir["url"] + f'&lang={lang}')
        directory = "fnapiio"

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(f"{directory}/" + dir["path"] + f'_{lang}.json', "w") as file:
            json.dump(data, file, indent=4)
            print("Data saved to file")

        time.sleep(2)
