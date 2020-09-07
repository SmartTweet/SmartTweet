import tweepy
from settings import settings

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

# access_token = r"application"
# access_token_secret = r"code de l'application"
# auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# print("get authorization: ", auth.get_authorization_url())
# get authorization:  https://api.twitter.com/oauth/authorize?oauth_token=Y7t4wwAAAAABHeo_AAABdGnHwIw

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
# 'message': 'Your credentials do not allow access to this resource', 'code': 220
# Echec car on est pas identifié comme application

tweets = api.search(q="Code Lyoko", result_type="recent", count=1)
for tweet in tweets:
    print(tweet)
print(len(tweets))
