from requests import get
from bs4 import BeautifulSoup

# URL of site we want to scrape
URL = "https://talkpython.fm/episodes/all"


def pull_site():
    raw_site_page = get(URL)  # Pull down the site.
    raw_site_page.raise_for_status()  # Confirm site was pulled. Error if not
    return raw_site_page


def scrape(site):
    # Create BeautifulSoup object
    soup = BeautifulSoup(site.text, 'html.parser')
    episode_list = soup.table.find_all('tr')

    filename = 'list_of_episodes.txt'
    print('Writing file containing the list of all talkpython episodes')
    with open(filename, 'w+', encoding='utf-8') as list_of_episodes:
        for episode in episode_list[1:]:
            list_of_episodes.write(episode.getText())

    print('Done')


if __name__ == "__main__":
    site = pull_site()
    scrape(site)
