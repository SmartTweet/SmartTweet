import twitter
import azure
from app.model.tweet import Tweet
from app.data_access.db_access import Db_Access


def get_analyses(ma_recherche: str, nbr_result: int):
    raw_tweet_list = twitter.twitter_api.recherche(ma_recherche, nbr_result)

    tweet_list = Tweet.from_raw_list(raw_tweet_list, ma_recherche)

    print(len(tweet_list))

    documents = azure.azure_api.from_tweetlist_to_documents(frozenset(tweet_list))
    azure_json = azure.azure_api.sentiments(documents)

    tweet_list = Tweet.from_azure_response(tweet_list, azure_json)

    return tweet_list


if __name__ == "__main__":
    tweet_list = get_analyses("samsung", 11)

    Db_Access.insert_tweet(tweet_list)
