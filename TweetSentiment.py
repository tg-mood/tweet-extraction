from textblob import TextBlob

class TweetSentiment():
    
    def __init__(self, text):
        self.text = TextBlob(text)
        self.frase = self.regulation()

    def isEnglish(self):
        return self.text.detect_language() == 'en'

    def regulation(self):
        if (not self.isEnglish()):
            traducao = str(self.text.translate(to="en"))
            return TextBlob(traducao)
        return self.text

    def result(self):
        return "Texto: {} - Polaridade: {}".format(self.frase, self.frase.sentiment.polarity)


