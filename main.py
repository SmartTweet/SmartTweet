from flask import Flask, request
from flask_cors import CORS

import twitter
import azure


def get_sentiments(ma_recherche: str):
    tweets_list = twitter.twitter_api.recherche(ma_recherche)

    documents = azure.azure_api.from_tweetlist_to_documents(tweets_list)
    documents = azure.azure_api.filter_language(documents)
    azure_json = azure.azure_api.sentiments(documents)

    # print(azure_json)
    return azure_json


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def homepage():
        hashtag = request.args.get('hashtag')

        if hashtag is not None:
            return get_sentiments(hashtag)

        return {}

    return app


if __name__ == "__main__":
    response = get_sentiments("#PNL")
    print(response)
