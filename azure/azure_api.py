import requests


class azure_api:

    __subscription_key = "8ada2411512a4dadb2add92f6e63291b"
    __endpoint = "https://cs-groupe-deux.cognitiveservices.azure.com/"
    __sentiment_url = __endpoint + "/text/analytics/v3.0/sentiment"

    @staticmethod
    def from_tweetlist_to_documents(tweets_list):
        list_document = []
        while tweets_list:
            tweets = tweets_list[:10]
            tweets_list = tweets_list[10:]

            analyse_list = []
            for tweet in tweets:
                analyse_list.append({
                    'id': tweet.id_tweet_twitter,
                    'language': tweet.language,
                    'text': tweet.content
                })

            list_document.append({"documents": analyse_list})
        return list_document


    @classmethod
    def sentiments(cls, documents: dict):
        """sentiments method takes documents variable as the following structure:

        Args:
            documents (dictionnary): azure structure for sentiments analysis

        Returns:
            str: result of the azure sentiments analysis as json string
        """
        headers = {"Ocp-Apim-Subscription-Key": cls.__subscription_key}
        response = requests.post(
            cls.__sentiment_url,
            headers=headers,
            json=documents
        )

        return response.json()
