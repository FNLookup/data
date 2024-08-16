from selenium import webdriver
import json
import time
import os

# two times because it bugs out
languages = ['en-US']
base_url = 'https://fortnite.com'
print("Initializing firefox")
driver = webdriver.Firefox()

directory = "page"
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    timestamps = {}
    for lang in languages:

        url = f'{base_url}?lang={lang}'

        if lang == "en-US":
            url = base_url
            time.sleep(15)

        driver.get(url)
        
        timestamp = time.time()
        timestamps[lang] = timestamp
        
        variable_data = driver.execute_script('return window.__remixContext;')
        
        if variable_data:
            filename = f'page/context_{lang}.json'
            with open(filename, 'w') as f:
                json.dump(variable_data, f, indent=4)
            print(f"Data saved to {filename}")
        else:
            print(f"Object not found for language {lang}")
    
    with open('page/timestamp.json', 'w') as f:
        json.dump(timestamps, f, indent=4)
    print("Timestamps saved to timestamps.json")
except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
