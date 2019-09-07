import tweepy
import re

class TwitterFeatures:
    
    def __init__(self, auth):
        self.auth = auth
        self.api = tweepy.API(self.auth)

    def clearTweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-ZÀ-Úa-zà-ú \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def getUserTimeline(self, id):
        
        try:
            results = [tweet.text for tweet in self.api.user_timeline(id=id, count=50)]

        except tweepy.error.TweepError as e:
            self.api.create_friendship(id)
            print("Deixe-nos te seguir para ter sua timeline analisada!")
            return False

        return [self.clearTweet(tweet).replace("RT", "").strip() for tweet in results if len(self.clearTweet(tweet)) > 3]
    