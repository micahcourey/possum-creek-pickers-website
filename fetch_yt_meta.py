import urllib.request
import json

urls = [
    "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=Usp1H0ny8wE&format=json",
    "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=htk9W0bEolc&format=json",
    "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=uuaCExW0Gwg&format=json"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print("TITLE:", data.get('title'))
            print("AUTHOR:", data.get('author_name'))
            print("---")
    except Exception as e:
        print("ERR:", e)
