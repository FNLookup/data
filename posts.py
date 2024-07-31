import os
import requests
import json
import time

language_list = ['en-US']
                # All
categories_list = ['', 'battle-royale', 'fortnite-festival', 'lego-fortnite', 'rocket-racing'] # Ditching the other categories cause whos gonna see that

fetch_list = [
    {
        "url": "https://www.fortnite.com/api/blog/getPosts?postsPerPage=0&offset=0&rootPageSlug=blog", # Adds language (&locale=) after and category after (&category=)
        "path": "blog_posts_category_lang_page_0.json" # Replace lang with language and category with category
    },{
        "url": "https://www.fortnite.com/api/blog/getPosts?postsPerPage=13&offset=13&rootPageSlug=blog",
        "path": "blog_posts_category_lang_page_1.json"
    }
]

timestamps = {}

markdown_string = '# Index - Blog Posts\n'

def format_category(script):
    words = script.split("-")
    formatted_words = [word.capitalize() for word in words]
    formatted_script = " ".join(formatted_words)
    
    return formatted_script

def get_page(input_string):
    digits = ""
    
    for char in input_string:
        if char.isdigit():
            digits += char
    
    try:
        result = int(digits)
    except ValueError:
        result = None
    
    return result

directory = "posts"
if not os.path.exists(directory):
    os.makedirs(directory)

def fetch_fortnite_posts(url):
    # url = 'https://www.fortnite.com/api/blog/getPosts?category=&postsPerPage=0&offset=0&locale=en-US&rootPageSlug=blog'
    headers = {
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US',
        'Referer': 'https://www.fortnite.com/news',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Success:", response.status_code)
        return response.json()
    else:
        print(f"Failed to fetch Fortnite API: {response.status_code}")
        print("Response content:", response.content)
        return None

if __name__ == "__main__":
    for language in language_list:

        markdown_string += f'\n## {language}\n|Entry|File|\n|-|-|\n'

        for category in categories_list:

            path_category = category

            if path_category == '':
                path_category = 'all'

            for fetch in fetch_list:

                url = fetch['url'] + f'&locale={language}&category={category}'
                print("GET:", url)
                print("Language:", language)
                print("Category:", path_category)

                fortnite_posts = fetch_fortnite_posts(url)
                if fortnite_posts:
                    path = fetch["path"].replace('category', path_category).replace('lang', language)
                    with open("posts/" + path, "w") as file:
                        json.dump(fortnite_posts, file, indent=4)
                        print(f'Data saved to file: posts/{path}')
                    timestamps[path.replace('.json', '')] = time.time()

                markdown_string += f'|{format_category(path_category)} #{get_page(path) + 1}|[{path}](https://github.com/FNLookup/data/blob/main/posts/{path})|\n'

                time.sleep(2)

            time.sleep(5)

        time.sleep(6)

        # Yep i actually had to add THREE TIME SLEEP calls.


    with open("posts/timestamps.json", "w") as file:
        json.dump(timestamps, file, indent=4)

        print("Timestamps saved to file")

    with open("posts/README.md", "w") as file:
        file.write(markdown_string)
        print("Markdown saved to file")
