from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey, Float, Date
from app.data_access.db_access import Db_Access
from sqlalchemy.orm import relationship, backref


class Tweet(Db_Access.BASE):

    __tablename__ = 'tweet'

    id_tweet = Column(Integer, primary_key=True)
    id_tweet_twitter = Column(String)
    content = Column(String)
    sentiment = Column(String)
    confident_level = Column(Float)
    hashtag = Column(String)
    date = Column(Date)

    def __init__(self, id_tweet_twitter, content, hashtag, date, language):
        self.id_tweet_twitter = id_tweet_twitter
        self.content = content
        self.hashtag = hashtag
        self.date = date
        self.language = language

    def set_analysis(self, sentiment, confident_level):
        self.sentiment = sentiment
        self.confident_level = confident_level

    def __str__(self):
        return (
            self.id_tweet_twitter + " " +
            self.sentiment + " " +
            self.confident_level + " " +
            self.date + " " +
            self.content
        )

    @classmethod
    def from_azure_response(cls, tweet_list, azure_json):
        for tweet in tweet_list:
            for analysis in azure_json['documents']:
                if str(tweet.id_tweet_twitter) == str(analysis['id']):
                    tweet.set_analysis(
                        analysis['sentiment'],
                        analysis['confidenceScores'][analysis['sentiment']]
                    )
                    break
        return tweet_list

    @classmethod
    def from_raw_list(cls, raw_tweet_list: list, hashtag: str):

        raw_tweet_list = filter(cls.__filter_language, raw_tweet_list)

        # tweet_list = list()
        # for tweet in raw_tweet_list:
        #     tweet_list.append(cls(
        #         tweet.id,
        #         tweet.text,
        #         hashtag,
        #         tweet.created_at
        #     ))

        # return tweet_list

        return [
            cls(
                tweet.id,
                tweet.text,
                hashtag,
                tweet.created_at,
                tweet.metadata['iso_language_code']
            ) for tweet in raw_tweet_list
        ]

    @staticmethod
    def __filter_language(tweet: dict):
        supported_languages = [
            "de", "en", "es", "fr", "it",
            "ja", "ko", "nl", "no", "pt-PT",
            "tr", "zh-Hans", "zh-Hant"
        ]

        if any(lang in tweet.metadata['iso_language_code'] for lang in supported_languages):
            return True
        else:
            return False
