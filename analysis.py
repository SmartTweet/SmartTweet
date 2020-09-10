class analysis:
    def __init__(self, id, text, hashtag, date):
        self.__id = id
        self.__text = text
        self.__hashtag = hashtag
        self.__date = date

    def __str__(self):
        if self.sentiment or self.sentiment_score:
            return self.hashtag + " " + self.sentiment + " " + "{:.0%}".format(self.sentiment_score) + " " + self.text
        else:
            return self.hashtag + " " + self.text

    def set_analysis(self, sentiment, sentiment_score):
        self.__sentiment = sentiment
        self.__sentiment_score = sentiment_score
