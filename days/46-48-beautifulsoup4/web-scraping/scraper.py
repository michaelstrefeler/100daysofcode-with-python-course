from requests import get
from bs4 import BeautifulSoup

# URL of site we want to scrape
URL = "https://pybit.es/pages/projects.html"


def pull_site():
    raw_site_page = get(URL)  # Pull down the site.
    raw_site_page.raise_for_status()  # Confirm site was pulled. Error if not
    return raw_site_page


def scrape(site):
    # Create BeautifulSoup object
    soup = BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.projectHeader')

    header_list = [header.getText() for header in html_header_list]

    for headers in header_list:
        print(headers)


if __name__ == "__main__":
    site = pull_site()
    scrape(site)
