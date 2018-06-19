import requests, feedparser

URL = 'http://www.thehindu.com/business/markets/feeder/default.rss'

def main():
    resp = requests.get(URL)

    with open('hindu_rss.xml', 'wb') as rss_file:
        rss_file.write(resp.content)

    feed = feedparser.parse('hindu_rss.xml')

    for entry in feed.entries:
        print(f'{entry.title}-{entry.link}')


if __name__ == '__main__':
    main()
