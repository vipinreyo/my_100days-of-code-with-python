from collections import namedtuple, Counter
import os
import re
import tweepy
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_ACCOUNT = 'vipinreyo'
TWITTER_KEY = os.getenv('TWITTER_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)


def main():
    tweets = list(get_tweets())

    exclu_rts = [tweet for tweet in tweets if not tweet.text.startswith('RT')]
    top_10 = sorted(exclu_rts, key=lambda tw: (tw.likes + tw.rts)/2, reverse=True)

    fmt = '{likes:<5} | {rts:<5} | {text}'

    print('{:<5} | {:<5} | Tweet text'.format('Likes', 'Retweets'))
    print('-'*150)

    for tw in top_10[:10]:
        print(fmt.format(likes=tw.likes, rts=tw.rts, text=tw.text))

    print()
    hashtags = re.compile(r'#[-_A-Za-z0-9]+')
    mentions = re.compile(r'@[-_A-Za-z0-9]+')

    all_tweets = ''.join([tw.text for tw in tweets])
    all_tweets_except_rt = ''.join([tw.text for tw in tweets if not tw.text.startswith('RT')])

    hashtags = hashtags.findall(all_tweets)
    cnt = Counter(hashtags)

    for tag in cnt.most_common(20):
        print(tag)

    mentions = mentions.findall(all_tweets_except_rt)
    cnt = Counter(mentions)

    for mention in cnt.most_common(20):
        print(mention)


def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exlude_replies=False, include_rts=True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)


if __name__ == '__main__':
    main()
