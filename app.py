import azure_api
import os
from flask import Flask, render_template,send_file
import json

app = Flask(__name__, template_folder="template")

@app.route('/tweet')
def hello_world():
    document_path = os.getcwd()+ os.sep + "out.csv" 
    document = open(document_path, "r", encoding="utf-8").readlines()
    document_path2 = os.getcwd()+ os.sep + "sentiments.csv"
    document2 = open(document_path2, "r", encoding="utf-8").readlines()



    result = json.loads(azure_api.get_sentiment())
    return render_template(
        "html_flask.html",
        titre0="Ce projet vous est présenté par : ",
        titre="Récuperation des tweets : Playstation 5",
        corps=result,
        titre2="Analyse des sentiments",
        corps2=document
    )

app.run(port = 8080, host = "localhost")


@app.route("/image/tweet.jpeg")
def send_image():
    return send_file("image/tweet.jpeg")

@app.route("/image/equipe.jpg")
def send_image2():
    return send_file("image/equipe.jpg")

@app.route("/template/tweet.css")
def send_css():
    return send_file("template/tweet.css")
