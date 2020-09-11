import json
import requests
from pprint import pprint
#import tweepy_test
import twitter_credentials as tc
import azure
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

keys = tc.Settings

endpoint = keys.AZURE_ENDPOINT
api_version = '?api-version=2020-06-30'
headers = {'Content-Type': 'application/json',
        'api-key': keys.API_AZURE_KEY}



def authenticate_client():
    ta_credential = AzureKeyCredential(keys.API_AZURE_KEY)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis_example(client):
    with open('tweets.json') as json_data:
        data = json.load(json_data)
        
        for tweet in data:
            tweetlist = [tweet['Texte']]
            response = client.analyze_sentiment(documents = tweetlist)[0]
            print("Document Sentiment: {}".format(response.sentiment))
            print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
                response.confidence_scores.positive,
                response.confidence_scores.neutral,
                response.confidence_scores.negative,
            ))
            for idx, sentence in enumerate(response.sentences):
                print("Sentence: {}".format(sentence.text))
                print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
                print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                    sentence.confidence_scores.positive,
                    sentence.confidence_scores.neutral,
                    sentence.confidence_scores.negative,
                ))

sentiment_analysis_example(client)