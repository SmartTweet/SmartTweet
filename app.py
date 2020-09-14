
import os



from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/tweet')
def hello_world():
    document_path = os.getcwd()+ os.sep + "out.csv" 
    document = open(document_path, "r", encoding="utf-8").readlines()
    document_path2 = os.getcwd()+ os.sep + "sentiments.csv"
    document2 = open(document_path2, "r", encoding="utf-8").readlines()
    return render_template(
        "html_flask.html",
        titre="Récuperation des tweets : Playstation 5",
        corps=document,
        titre2="Analyse des sentiments",
        corps2=document2
    )

app.run(port = 8080, host = "localhost")

