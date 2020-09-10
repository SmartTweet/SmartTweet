from flask import Flask, render_template, jsonify
from app.data_access.db_access import Db_Access


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
            print(type(Db_Access.get_all()))
            print(type(Db_Access.get_all()[0]))
            return jsonify([
                tweet.__dict__ for tweet in Db_Access.get_all()
            ])
        else:
            return jsonify([
                tweet.__dict__ for tweet in Db_Access.get_tweets_by_hashtag(hashtag)
            ])
    return app
