



import requests
import os
import json

# Pour définir vos variables d'environnement dans votre terminal, exécutez la ligne suivante:
# export 'BEARER_TOKEN' = '<your_bearer_token>'


def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url():
    query = "from:twitterdev -is:retweet"
    
    # Les champs Tweet sont ajustables.
    # Les options comprennent:
    # pièces jointes, author_id, context_annotations,
    # conversation_id, created_at, entités, géo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # éventuellement_sensitive, promise_metrics, public_metrics, referenced_tweets,
    # source, texte et retenu
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()