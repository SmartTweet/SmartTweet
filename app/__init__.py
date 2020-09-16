from flask import Flask, jsonify
from flask_cors import CORS

import app.data_access as dal

app = Flask(__name__)
CORS(app)


@app.route('/')
@app.route('/index')
def index():
    return "Bienvenue sur le serveur back !"


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

# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory(web_folder + '/js', path)


# @app.route('/css/<path:path>')
# def send_css(path):
#     return send_from_directory(web_folder + '/css', path)


# @app.route('/img/<path:path>')
# def send_img(path):
#     return send_from_directory(web_folder + '/img', path)