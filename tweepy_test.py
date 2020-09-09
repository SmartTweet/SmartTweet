import tweepy
from settings import settings

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

api = tweepy.API(auth)

tweets = api.search(q="playstation", result_type="recent", count=1)

for tweet in tweets:
    print(tweet.text)
print(len(tweets))



