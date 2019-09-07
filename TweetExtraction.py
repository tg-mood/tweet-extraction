import json
import tweepy
from UserAuth import UserAuth
from TwitterFeatures import TwitterFeatures

with open("twitterKeys.json") as json_file:
    keys = json.load(json_file)
    consumer_key = keys['consumer_key']
    consumer_secret = keys['consumer_secret']
    access_token = keys['access_token']
    access_secret = keys['access_secret']

userAuth = UserAuth(consumer_key, consumer_secret, access_token, access_secret)
userAuth.setToken()
auth = userAuth.createAuth()

twitterFeatures = TwitterFeatures(auth)

tweets = twitterFeatures.getUserTimeline("realdonaldtrump")

if(tweets):
    for tweet in tweets:
        print(tweet)
else:
    print("Um erro ocorreu!")
