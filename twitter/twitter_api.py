import tweepy
import twitter


class twitter_api:
    api = tweepy.API(tweepy.OAuthHandler(
            twitter.settings.CONSUMER_KEY,
            twitter.settings.CONSUMER_SECRET
        )
    )

    @classmethod
    def recherche(cls, ma_recherche: str):
        tweets = cls.api.search(q=ma_recherche + " -RT", count=10)
        # "-RT" should remove retweets (i'm not sure)
        return [
            [tweet.id, tweet.metadata['iso_language_code'], tweet.text]
            for tweet in tweets
        ]


if __name__ == "__main__":
    tweets_text = twitter_api.recherche("Cofee")

    for tweet in tweets_text:
        print(tweet)
