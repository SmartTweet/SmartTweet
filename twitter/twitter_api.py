import tweepy
import twitter


class twitter_API:
    @staticmethod
    def recherche(ma_recherche: str):
        auth = tweepy.OAuthHandler(
            twitter.settings.CONSUMER_KEY,
            twitter.settings.CONSUMER_SECRET
        )
        api = tweepy.API(auth)

        tweets = api.search(q=ma_recherche, count=10)
        return [[tweet.id, tweet.metadata['iso_language_code'], tweet.text] for tweet in tweets]


if __name__ == "__main__":
    tweets_text = twitter_API.recherche("Cofee")

    for tweet in tweets_text:
        print(tweet)
