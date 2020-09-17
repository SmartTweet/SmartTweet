import tweepy
import twitter


class twitter_api:
    api = tweepy.API(tweepy.OAuthHandler(
            twitter.Settings.CONSUMER_KEY,
            twitter.Settings.CONSUMER_SECRET
        )
    )

    @classmethod
    def recherche(cls, ma_recherche: str, nbr_result: int):
        return cls.api.search(q="#" + ma_recherche + " -RT", count=nbr_result)
        # "-RT" should remove retweets (i'm not sure
