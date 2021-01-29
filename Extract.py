import tweepy
import pandas as pd
consumer_key = "j4kLoamWfoPbw72VLoQwjmzeF"
consumer_secret = "UwEGlKxK2xX4I59FXhwUmc1A4wPoW2ZceTY1ZI2iTdEGDOaOjY"
access_token = "1040311982015037440-1TSqPfFZmXn1fUS1qplchjVbWBMANn"
access_token_secret = "K0efO3na1D9Mw1Du7rkROzgOW8zDTLTG6AcVTuLqMzjQq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

text_query = '#MUFC  -filter:retweets'
count = 1000
try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search, q=text_query).items(count)

    # Pulling information from tweets iterable object
    tweets_list = [[tweet.id, tweet.user.screen_name, tweet.created_at, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    # Add or remove columns as you remove tweet information
    tweets_df = pd.DataFrame(tweets_list)
    tweets_df.columns = ['id', 'user', 'created_at', 'text']
    #  print(tweets_df.head(20))
    tweets_df.to_csv('tweets.csv', index=False)
except BaseException as e:
    print('failed on_status,', str(e))
