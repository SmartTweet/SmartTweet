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

    @app.route('/tweet/')
    @app.route('/tweet/<hashtag>')
    def tweet(hashtag: str = 'all'):
        if hashtag == 'all':

            tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_all()]
            for tweet in tweet_list:
                del tweet['_sa_instance_state']
            return jsonify(tweet_list)

        else:

            tweet_list = [tweet.__dict__ for tweet in dal.Db_Access.get_tweets_by_hashtag(hashtag)]
            for tweet in tweet_list:
                del tweet['_sa_instance_state']
            return jsonify(tweet_list)

    return app
