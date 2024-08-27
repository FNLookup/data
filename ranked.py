from selenium import webdriver
import json
import time
import os
import traceback

# two times because it bugs out
languages = ['en-US']
base_url = 'https://www.fortnite.com/ranked/leaderboard'
print("Initializing firefox")
driver = webdriver.Firefox()

directory = "page/ranked/lb/"
if not os.path.exists(directory):
    os.makedirs(directory)

rankedpage = 0
allpages = 1

try:
    # timestamps = {}
    for lang in languages:

        url = f'{base_url}?lang={lang}'

        driver.get(url)
        
        timestamp = time.time()
        # timestamps[lang] = timestamp

        while (rankedpage < allpages):
            result = str(driver.execute_script('fetch("https://www.fortnite.com/ranked/leaderboard?season=chapter-5-season-4&page=' + (rankedpage + 1) + 'lang=en-US&_data=routes%2Franked.leaderboard._index").then(r=>r.text()).then(r => {return r});'))
            print(result)
            variable_data = json.loads(result)
            if variable_data:
                allpages = variable_data['leaderboard']['totalPages']
                time.sleep(2)
                filename = f'{directory}/lb{rankedpage}.json'
                with open(filename, 'w') as f:
                    json.dump(variable_data, f, indent=4)
                    print(f"Data saved to {filename}")

                rankedpage += 1
        else:
            print('finished on page', rankedpage)
except Exception as e:
    traceback.print_exc()
    print("Error:", e)
finally:
    driver.quit()
