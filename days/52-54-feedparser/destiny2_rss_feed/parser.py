import feedparser

FEED_FILE = 'NewsRss.xml'

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for ent in feed.entries:
        if ent.description:
            print(
                f"{ent.published} - {ent.title}: {ent.description} {ent.link}")
        else:
            print(f"{ent.published} - {ent.title}: {ent.link}")
else:
    print("Tag not found.")
