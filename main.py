import twitter
import azure


def get_sentiments(ma_recherche: str):
    tweets_list = twitter.twitter_api.recherche(ma_recherche)

    documents = azure.azure_api.from_tweetlist_to_documents(tweets_list)
    documents = azure.azure_api.filter_language(documents)
    azure_json = azure.azure_api.sentiments(documents)

    print(azure_json)
    exit()

    return azure_json


if __name__ == "__main__":
    response = get_sentiments("#PNL")
    print(response)
