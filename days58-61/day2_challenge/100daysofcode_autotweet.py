from config import api
import requests
import re

TWEET_LENGTH = 140
PROGRESS_LOG = 'https://raw.githubusercontent.com/vipinreyo/my_100days-of-code-with-python/master/log.md'


def get_progress_log():
    response = requests.get(PROGRESS_LOG)
    response.raise_for_status()
    #print(response.text)
    return response


def get_day_progress(log):
    current_progress = log.split('\n')[-2]
    match = re.search(r':.+\.\s', current_progress)
    return match.group().replace(': ', '')


def create_tweet(title):
    tweet_format = "Completed '{}' https://talkpython.fm/100days?s=pybites #Python @pybites @talkpython".format(title)
    return tweet_format


def tweet_progress():
    pass


def main():
    resp = get_progress_log()
    title = get_day_progress(resp.text)
    print(create_tweet(title))


if __name__ == '__main__':
    main()
