import twitter
import azure
from analysis import analysis


def get_analyses(ma_recherche: str):
    tweets_list = twitter.twitter_api.recherche(ma_recherche)

    documents = azure.azure_api.from_tweetlist_to_documents(tweets_list)
    azure_json = azure.azure_api.sentiments(documents)

    print(len(azure_json['documents']), '\n')
    for sentiment in azure_json['documents']:

        total_text = str()
        for sentence in sentiment['sentences']:
            total_text += sentence['text']

        analysis_list.append(
            analysis(
                sentiment['id'],
                sentiment['sentiment'],
                sentiment['confidenceScores'][sentiment['sentiment']],
                total_text,
                ma_recherche
            )
        )

    return analysis_list


if __name__ == "__main__":
    liste_analyses = get_analyses("#PNL")
    print(list(map(str, liste_analyses)))
