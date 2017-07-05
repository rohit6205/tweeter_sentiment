import tweepy
from textblob import TextBlob

consumer_key= ' PUT YOUR TWEETER CONSUMER KEY'
consumer_secret= ' PUT YOUR TWEETER CONSUMER_SECRET'

access_token=' PUT YOUR TWEETER ACCESS_TOKEN'
access_token_secret=' PUT YOUR TWEETER ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")