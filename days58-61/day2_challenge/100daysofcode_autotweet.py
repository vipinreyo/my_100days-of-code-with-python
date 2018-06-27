from config import api
import requests
import re

TWEET_LENGTH = 140
PROGRESS_LOG = 'https://raw.githubusercontent.com/vipinreyo/my_100days-of-code-with-python/master/log.md'


def get_progress_log():
    response = requests.get(PROGRESS_LOG)
    response.raise_for_status()
    return response


def get_day_progress(log):
    current_progress = log.split('\n')[-2]
    match = re.search(r':.+\.\s', current_progress)
    return match.group().replace(': ', '')


def create_tweet(title):
    tweet_format = "Completed '{}' https://talkpython.fm/100days?s=pybites #Python @pybites " \
                   "@talkpython #automated".format(title)
    return tweet_format


def tweet_progress(tweet):
    try:
        api.update_status(tweet)
        print('Posted to twitter account')
    except Exception as ex:
        print('Unable to post to twitter. {}'.format(ex))


def main():
    resp = get_progress_log()
    title = get_day_progress(resp.text)
    tweet = create_tweet(title)
    tweet_progress(tweet)


if __name__ == '__main__':
    main()
