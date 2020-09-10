# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Db_Access():

    __ENGINE = create_engine('postgresql://rjrfriyt:Yzslx9R-wgaR1-pv0FNxiYzpKDjXb62K@lallah.db.elephantsql.com/rjrfriyt')
    __SESSION = sessionmaker(bind=__ENGINE)
    BASE = declarative_base()

    '''
    insert new tweets
    '''
    @classmethod
    def insert_tweet(cls, data_list):
        session = cls.__SESSION()
        for data in data_list:
            session.add(data)
        session.commit()
        session.close()

    '''
    return all tweets
    '''
    @classmethod
    def get_all(cls):
        from app.model.tweet import Tweet
        session = cls.__SESSION()
        return session.query(Tweet).all()

    '''
    return list of tweets filtered by hashtag
    '''
    @classmethod
    def get_tweets_by_hashtag(cls, hashtag):
        session = cls.__SESSION()
        return session.query(Tweet).filter(Tweet.hashtag == hashtag).all()
