# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Db_Access():

    ENGINE = create_engine('postgresql://rjrfriyt:Yzslx9R-wgaR1-pv0FNxiYzpKDjXb62K@lallah.db.elephantsql.com/rjrfriyt')
    SESSION = sessionmaker(bind=ENGINE)
    BASE = declarative_base()

    '''
    insert new tweets
    '''
    def insert_tweet(self, data_list):
        session = self.SESSION()
        for data in data_list:
            session.add(data)
        session.commit()
        session.close()

    '''
    return all tweets
    '''
    def get_all(self, table):
        session = self.SESSION()
        return session.query(table).all()

    '''
    return list of tweets filtered by hashtag
    '''
    def get_tweets_by_hashtag(self, hashtag):
        from model.tweet import Tweet
        session = self.SESSION()
        return session.query(Tweet).filter(Tweet.hashtag == hashtag).all()
