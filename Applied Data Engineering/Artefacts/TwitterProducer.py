import tweepy
import json
from confluent_kafka import Producer
from config import consumer_key, consumer_secret, access_token_secret, access_token_key, conf, coin_symbols

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

### create producer
producer = Producer(conf)

### create hashtag list
coin_hashtags = []
for coin in coin_symbols:
    coin_hashtags.append('#' + coin)


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        if not decoded['text'].startswith('RT'):
            producer.produce("Twitter_data", json.dumps(decoded))
            producer.flush()
            print(decoded)


def start_stream():
    while True:
        try:
            myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
            myStream.filter(track=coin_hashtags)
        except:
            continue


start_stream()