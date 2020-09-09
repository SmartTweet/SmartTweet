import requests
# pprint is used to format the JSON response
from pprint import pprint


# Créez des variables pour le point de terminaison et la clé d’abonnement Azure de votre ressource.
subscription_key = "8ada2411512a4dadb2add92f6e63291b"
endpoint = "https://cs-groupe-deux.cognitiveservices.azure.com/"

language_api_url = endpoint + "/text/analytics/v3.0/languages"          
# Pour détecter le sentiment (positif ou négatif) d’un jeu de documents,
# ajoutez /text/analytics/v3.0/sentiment au point de terminaison de base d’Analyse de texte pour former
# l’URL de détection de langue. 
# Par exemple : https://<your-custom-subdomain>.cognitiveservices.azure.com/text/analytics/v3.0/sentiment

sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"                 


# documents = {"documents": [
#     {"id": "1", "language": "en",
#         "text": "I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable."},
#     {"id": "2", "language": "es",
#         "text": "Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico."}
# ]}

documents = {"documents": [
    {"id": "1", "language": "en",
        "text": "RT @MyTekReview: Which one will you buy ? Vote and comment why you make a decision  .."},
    
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)








