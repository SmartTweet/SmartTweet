import requests
from app.model.tweet import Tweet


class azure_api:

    __subscription_key = "8ada2411512a4dadb2add92f6e63291b"
    __endpoint = "https://cs-groupe-deux.cognitiveservices.azure.com/"
    __sentiment_url = __endpoint + "/text/analytics/v3.0/sentiment"

    @staticmethod
    def from_tweetlist_to_documents(tweets_list):
        document_list = []
        for tweet in tweets_list:
            document_list.append({
                'id': tweet.id_tweet_twitter,
                'language': tweet.language,
                'text': tweet.content
            })

        return {"documents": document_list}

    @classmethod
    def sentiments(cls, documents: dict):
        """sentiments method takes documents variable as the following structure:

        {"documents": [
            {"id": "1", "language": "en",
                "text": "I really enjoy the new XBox One S."},
            {"id": "2", "language": "es",
                "text": "Este ha sido un dia terrible, llegué tarde ..."}
        ]}

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
