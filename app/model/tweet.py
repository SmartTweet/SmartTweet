from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey, Float
from dataaccess.db_access import Db_Access
from sqlalchemy.orm import relationship, backref

class Tweet(Db_Access.BASE):

    __tablename__ = 'tweet'

    id_tweet = Column(Integer, primary_key=True)
    id_tweet_twitter = Column(String)
    content = Column(String)
    sentiment = Column(String)
    confident_level = Column(Float)
    hashtag = Column(String)


    def __init__(self, id_tweet_twitter, content, sentiment, confident_level, hashtag):
        self.id_tweet_twitter = id_tweet_twitter
        self.content = content
        self.sentiment = sentiment
        self.confident_level = confident_level
        self.hashtag = hashtag