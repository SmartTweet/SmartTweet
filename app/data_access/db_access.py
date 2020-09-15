# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app.model as model


class Db_Access():

    __ENGINE = create_engine('postgresql://rjrfriyt:Yzslx9R-wgaR1-pv0FNxiYzpKDjXb62K@lallah.db.elephantsql.com/rjrfriyt')
    __SESSION = sessionmaker(bind=__ENGINE)

    '''
    insert new tweets
    '''
    @classmethod
    def insert_tweet(cls, data_list):
        session = cls.__SESSION()
        for data in data_list:
            data.hashtag = data.hashtag.lower()
            session.add(data)
        session.commit()
        session.close()

    '''
    return all tweets
    '''
    @classmethod
    def get_all(cls):
        session = cls.__SESSION()
        return session.query(model.Tweet).all()

    '''
    return list of tweets filtered by hashtag
    '''
    @classmethod
    def get_tweets_by_hashtag(cls, hashtag):
        session = cls.__SESSION()
        return session.query(model.Tweet).filter(
            model.Tweet.hashtag == hashtag.lower()).all()


    @classmethod
    def get_hashtags(cls):
        session = cls.__SESSION()

        return [row.hashtag for row in session.query(model.Tweet).distinct(model.Tweet.hashtag).all()]
