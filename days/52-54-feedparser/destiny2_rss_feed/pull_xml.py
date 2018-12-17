import requests

URL = 'https://www.bungie.net/News/NewsRss.ashx'

if __name__ == "__main__":
    r = requests.get(URL)
    with open('NewsRss.xml', 'wb') as f:
        f.write(r.content)
