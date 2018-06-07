
import requests
import bs4


def download_site(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def main():
    url = 'https://talkpython.fm/episodes/all'
    site = download_site(url)
    dom = bs4.BeautifulSoup(site.text, 'html.parser')

    anchors = dom.find('div', {'class': 'episodes'}).find('table').find_all('a')

    print('Talk python Episodes:')
    for a in anchors:
        print(a.string)


if __name__ == '__main__':
    main()
