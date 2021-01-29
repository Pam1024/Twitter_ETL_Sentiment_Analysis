from textblob import TextBlob
import csv
import re
import pandas as pd

def clean(input):
    input = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', input)
    input = re.sub(r'\bwth\b', 'what the hell', input)
    input = re.sub(r'\br\b', 'are', input)
    input = re.sub(r'\bu\b', 'you', input)
    input = re.sub(r'\bk\b', 'OK', input)
    input = re.sub(r'\bsux\b', 'sucks', input)
    input = re.sub(r'\bno+\b', 'no', input)
    input = re.sub(r'\bcoo+\b', 'cool', input)
    input = re.sub(r'\bthats\b', 'that is', input)
    input = re.sub(r'\bive\b', 'i have', input)
    input = re.sub(r'\bim\b', 'i am', input)
    input = re.sub(r'\bya\b', 'yeah', input)
    input = re.sub(r'\bcant\b', 'can not', input)
    input = re.sub(r'\bwont\b', 'will not', input)
    input = re.sub(r'\bid\b', 'i would', input)
    input = re.sub(r'wtf', 'what the fuck', input)
    input = re.sub(r'rip', 'rest in peace', input)
    input = re.sub(r'lol', 'laugh out loud', input)
    input = re.sub(r'lmao', 'laughing my ass off', input)
    return input

tweets_df = pd.read_csv('tweets.csv')
tweets_df['text'] = tweets_df['text'].apply(lambda x : clean(x))
tweets_df['TextBlob'] = tweets_df['text'].apply(lambda x : TextBlob(x))
tweets_df['polarity'] = tweets_df['TextBlob'].apply(lambda x : x.sentiment.polarity)

def sentiment(p):
    if p > 0.2:
        return 'positive'
    elif p < -0.2:
        return 'negative'
    else:
        return 'neutral'

tweets_df['sentiment'] = tweets_df['polarity'].apply(lambda x : sentiment(x))

tweets_df.rename(columns={'text': 'tweet','polarity': 'sentiment_score'},inplace=True)

tweets_df[['tweet','sentiment','sentiment_score']].to_csv('tweets_result.csv',index=False)