import tweepy
import keys
import pandas as pd
import numpy as np


cle = keys.Key
auth = tweepy.OAuthHandler(cle.API_TWITTER_KEYS, cle.API_TWITTER_SECRET_KEYS)
auth.set_access_token(cle.API_TWITTER_TOKEN, cle.API_TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

df = pd.DataFrame(columns=["id","language","date", "texte"])

for tweet in tweepy.Cursor(api.search,q="#GTO",count=1, lang = 'fr').items():
    
    liste_tweet = [tweet.id, tweet.lang, tweet.created_at, tweet.text.encode('utf-8')]
    ar = np.array([liste_tweet])
    df2 = pd.DataFrame(ar, columns=["id","language","date", "texte"])
    df = df.append(df2)
    
df.to_csv("out.csv")
