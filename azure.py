import requests
from pprint import pprint           # pprint is used to format the JSON response
import keys
import csv
import pandas as pd

# Créez des variables pour le point de terminaison et la clé d’abonnement Azure de votre ressource.
key_azure = "8ada2411512a4dadb2add92f6e63291b"
endpoint_azure = "https://cs-groupe-deux.cognitiveservices.azure.com/"

detection_langue = endpoint_azure + "/text/analytics/v3.0/languages"          
detection_sentiment = endpoint_azure + "/text/analytics/v3.0/sentiment"

with open("out.csv",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    tweet_list = []
    next(reader)
    for row in reader:
        tweet_list.append({
            "id" : row[1], 
            "language" : row[2], 
            "text" : row[4]
        })

documents = {"documents": tweet_list}

headers = {"Ocp-Apim-Subscription-Key": key_azure}
response = requests.post(detection_sentiment, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)

print("")

dyc = sentiments
 
sentiments = open('sentiments.csv', 'w')
mywriter = csv.writer(sentiments, delimiter=';', dialect='excel', lineterminator='\n')

mywriter.writerow(["id","sentiment","postivie", "neutre", "negative"])
 
for i in dyc["documents"]:
    mywriter.writerow([
        i["id"],
        i["sentiment"],
        str(i["confidenceScores"]["positive"]),
        str(i["confidenceScores"]["neutral"]),
        str(i["confidenceScores"]["negative"])
    ])

sentiments.close()
