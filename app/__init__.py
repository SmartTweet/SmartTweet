from flask import Flask, jsonify
from flask_cors import CORS

import app.data_access as dal

app = Flask(__name__)
CORS(app)


@app.route('/tweet/')
def get_all_tweet():
    tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_all()]
    for tweet in tweet_list:
        del tweet['_sa_instance_state']
    return jsonify(tweet_list)


@app.route('/api/tweet/<hashtag>')
def get_tweet(hashtag):
    # TODO Check #
    print(hashtag)
    if not hashtag:
        return []

    tweet_list = [
        tweet.__dict__ for tweet in dal.Db_Access.get_tweets_by_hashtag(
            hashtag)]

    print(len(tweet_list))
    for tweet in tweet_list:
        print(tweet)
        del tweet['_sa_instance_state']

    return jsonify(tweet_list)
