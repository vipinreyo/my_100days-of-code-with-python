import requests
import feedparser

URL = 'https://store.steampowered.com/feeds/news.xml'


def main():
    response = requests.get(URL)

    with open('new_releases.xml', 'wb') as xml_file:
        xml_file.write(response.content)

    parser = feedparser.parse('new_releases.xml')

    for entry in parser.entries:
        print(f'{entry.published}-{entry.title}-{entry.link}')


if __name__ == '__main__':
    main()
