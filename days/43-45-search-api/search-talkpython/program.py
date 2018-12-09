import requests
from collections import namedtuple
from random import randint
import webbrowser

Result = namedtuple('Result', 'category, description, id, title, url')


def get_results(keyword):
    url = f'http://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    amount = len(results['results'])

    if amount == 0:
        print(f'No results for {keyword} were found')
        exit()

    formatted_results = []

    for result in results['results']:
        formatted_results.append(Result(**result))

    return formatted_results

def show_results(formatted_results):
    for idx, item in enumerate(formatted_results):
        print(f"{idx+1}. {item.title}")

    amount = len(formatted_results)
    print("\nWhich result would you like to go to?")
    answer = input(f"Choose a numeber from 1 to {amount}: ")

    try:
        answer = int(answer)
    except ValueError:
        print('That was not a number, so I chose one for you')
        answer = randint(1, amount)

    full_url = 'https://talkpython.fm' + formatted_results[int(answer) - 1].url

    print(f'Opening {formatted_results[int(answer) - 1].title}')
    webbrowser.open(full_url, new=2)
    print('Done. Check your browser')
    
    return results


if __name__ == '__main__':
    keyword = input('What are you looking for on talkpython.fm? ')
    results = get_results(keyword)
    show_results(results)
