from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

import app.data_access as dal

web_folder = "../vuejs/"
app = Flask(
    __name__,
    template_folder=web_folder,
    static_folder=web_folder + 'static'
)
CORS(app)


@app.route('/')
@app.route('/index')
def index():
    return send_from_directory(web_folder, 'index.html')


@app.route('/api/tweets/')
def get_all_tweet():
    tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_all()]
    for tweet in tweet_list:
        del tweet['_sa_instance_state']
    return jsonify(tweet_list)


@app.route('/api/tweet/<hashtag>')
def get_tweet(hashtag):
    if not hashtag:
        return []

    tweet_list = [
        tweet.__dict__ for tweet in dal.Db_Access.get_tweets_by_hashtag(
            hashtag)]

    for tweet in tweet_list:
        del tweet['_sa_instance_state']

    return jsonify(tweet_list)


@app.route('/api/hashtags/')
def get_hashtags():
    return jsonify(dal.Db_Access.get_hashtags())
