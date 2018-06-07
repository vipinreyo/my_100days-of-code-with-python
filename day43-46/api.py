import requests
from collections import namedtuple
from pprint import pprint

Episode = namedtuple('Episode', 'category description id title url')


def search_talk_python_podcast(keyword: str):
    url = f'http://search.talkpython.fm/api/search?q={keyword}'
    response = requests.get(url)
    response.raise_for_status()
    results = response.json()

    episodes = []
    #pprint(results)
    for r in results['results']:
        #print(r)
        episodes.append(Episode(**r))

    return episodes
