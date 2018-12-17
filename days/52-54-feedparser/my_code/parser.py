import feedparser

FEED_FILE = 'newreleases.xml'

feed = feedparser.parse(FEED_FILE)

for entry in feed.entries:
    print(f"{entry.published} - {entry.title}: {entry.link}") 