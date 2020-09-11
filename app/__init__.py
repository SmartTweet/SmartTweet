from flask import Flask
import requests
from ..main import get_sentiments


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        hashtag = requests.args.get('hashtag')
        return get_sentiments(hashtag)

    return app
