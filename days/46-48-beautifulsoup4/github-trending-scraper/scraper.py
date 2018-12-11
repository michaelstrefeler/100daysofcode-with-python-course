from requests import get
from bs4 import BeautifulSoup

URL = "https://github.com/trending"


def pull_site():
    raw_site_page = get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    soup = BeautifulSoup(site.text, 'html.parser')
    repos = soup.find_all('li', 'col-12 d-block width-full py-4 border-bottom')
    print("Trending repos on GitHub")
    for tag in repos:
        link = 'https://github.com' + tag.a.get("href")
        name = tag.a.getText()
        print(name, link)


if __name__ == "__main__":
    site = pull_site()
    scrape(site)
