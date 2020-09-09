from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('homepage.html')

    return app
