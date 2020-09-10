import json
import requests
from pprint import pprint
#import tweepy_test
import twitter_credentials as tc
import azure
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

keys = tc.settings

endpoint = keys.AZURE_ENDPOINT
api_version = '?api-version=2020-06-30'
headers = {'Content-Type': 'application/json',
        'api-key': keys.API_AZURE_KEY }



def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()