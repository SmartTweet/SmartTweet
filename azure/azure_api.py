import requests


class azure_api:

    __subscription_key = "8ada2411512a4dadb2add92f6e63291b"
    __endpoint = "https://cs-groupe-deux.cognitiveservices.azure.com/"
    __sentiment_url = __endpoint + "/text/analytics/v3.0/sentiment"

    @staticmethod
    def from_tweetlist_to_documents(tweets_list: list):
        document_list = []
        for tweet in tweets_list:
            document_list.append({
                'id': tweet[0],
                'language': tweet[1],
                'text': tweet[2]
            })

        return {"documents": document_list}

    @staticmethod
    def filter_language(documents: dict):
        filtered_list = []
        supported_languages = [
            "de", "en", "es", "fr", "it",
            "ja", "ko", "nl", "no", "pt-PT",
            "tr", "zh-Hans", "zh-Hant"
        ]

        for tweet in documents['documents']:
            if any(lang in tweet['language'] for lang in supported_languages):
                filtered_list.append(tweet)

        return {"documents": filtered_list}

    @classmethod
    def sentiments(cls, documents: dict):
        """sentiments method takes documents variable as the following structure:

        {"documents": [
            {"id": "1", "language": "en",
                "text": "I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable."},
            {"id": "2", "language": "es",
                "text": "Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico."}
        ]}

        Args:
            documents (dictionnary): azure document structure for sentiments analysis

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
