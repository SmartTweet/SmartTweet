import twitter

tweets_list = twitter.twitter_API.recherche("Cofee")

tweets_dict = dict()
for tweet in tweets_list:
    tweets_dict['id'] = tweet[0]
    tweets_dict['lang'] = tweet[1]
    tweets_dict['text'] = tweet[2]

for t_text in tweets_text:
    print(t_text)

