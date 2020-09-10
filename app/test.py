from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dataaccess.db_access import Db_Access
from model.tweet import Tweet

# instantiate a database access
db = Db_Access()

# create a list of tweets for test
tweet_list = []

# fill the list with tweets
tweet_list.append(Tweet('323K2K3L2', 'tweet 1', 'positif', 0.6, 'Samsung'))
tweet_list.append(Tweet('Y9SD8DS0D', 'tweet 2', 'neutral', 0.5, 'Samsung'))
tweet_list.append(Tweet('2LSD9809S', 'tweet 3', 'negative', 0.2, 'Samsung'))

# insert tweet list
#db.insert_tweet(tweet_list)

# get all tweets
tweets = db.get_all(Tweet)

# get tweets by hashtag
tweets_by_hashtag = db.get_tweets_by_hashtag("Samsung")

    
print('')