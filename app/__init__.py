from flask import Flask, render_template, jsonify
import app.data_access as dal


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('homepage.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name='diallo'):
        return render_template('hello.html', name=name)

    @app.route('/tweet/', method='GET')
    def get_all_tweet():
        tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_all()]
        for tweet in tweet_list:
            del tweet['_sa_instance_state']
        return jsonify(tweet_list)

    """
    Problème: une url de type /tweet/#NVIDIA sera coupée au niveau du "#"
        Donc impossible d'utiliser '/tweet/<hashtag>'
    """
    # @app.route('/tweet/<hashtag>', method='GET')
    # def get_tweet(hashtag):

    #     if not hashtag:
    #         return []

    #     tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_tweets_by_hashtag(hashtag)]
    #     for tweet in tweet_list:
    #         del tweet['_sa_instance_state']
    #     return jsonify(tweet_list)

    @app.route('/tweet/', method='POST')
    def get_tweet():

        # recuperer le hashtag:
        print("DEBUG: GET == ", str(request.POST))
        hashtag = request.POST['hashtag']

        tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_tweets_by_hashtag(hashtag)]
        for tweet in tweet_list:
            del tweet['_sa_instance_state']
        return jsonify(tweet_list)

    return app
