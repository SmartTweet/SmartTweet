import tweepy
from tweepy.auth import OAuthHandler
import twitter_credentials as tc
import csv 
import json



keys = tc.Settings()


auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



dico_tweet = []
for tweet in tweepy.Cursor(api.search,q="#rtx3080",count=100, lang = 'fr').items():
    if tweet.retweeted == False:
        temp = {}
        temp['Date'] = tweet.created_at.strftime('%Y-%d-%m')
        temp['Auteur'] = tweet.user.screen_name
        temp['Texte'] = tweet.text
        dico_tweet.append(temp)

with open('tweets.json', 'w') as json_file:
    json.dump(dico_tweet, json_file)

        #print (tweet.created_at.strftime("%Y-%d-%m"), tweet.text)
        #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])