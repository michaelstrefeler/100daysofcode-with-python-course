import requests


def search_talkpython(keyword):
    url = f'http://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()

    for item in results['results']:
        print(item['title'])

    return results


if __name__ == '__main__':
    keyword = input('What are you looking for on talkpython.fm? ')
    search_talkpython(keyword)
