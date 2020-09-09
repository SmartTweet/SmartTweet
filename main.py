import twitter
import azure


def get_sentiments(ma_recherche):
    tweets_list = twitter.twitter_api.recherche(ma_recherche)

    documents = azure.azure_api.from_tweetlist_to_documents(tweets_list)
    azure_response_json = azure.azure_api.sentiments(documents)

    return azure_response_json


if __name__ == "__main__":
    response = get_sentiments("Cofee")
    print(response)
