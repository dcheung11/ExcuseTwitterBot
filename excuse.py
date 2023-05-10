import requests
import tweepy
import os
import time
from datetime import datetime

# api_key=
# api_secret=
# bearer_token=
# access_token=
# access_token_secret=
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_token_secret)
 
api = tweepy.API(auth)

# Fetch the excuse from a Excuser API
def fetch_excuse():
    response = requests.get('https://excuser-three.vercel.app/v1/excuse')
    excuse = response.json()[0]['excuse']
    category = response.json()[0]['category']
    return (excuse, category)

# Post a tweet with a given message
def post_tweet(excuse, category):
    tweet_text = "DameBot's excuse of the day: \n" + excuse + "\n#" + category + " #DameBot"
    client.create_tweet(text = tweet_text)

    
#     Instead, hosted on PythonAnywhere
# while True:
# now = datetime.utcnow()
# Check if it's time to tweet
# if now.hour == 13 and now.minute == 0:
excuse, category = fetch_excuse()
post_tweet(excuse,category)
# Wait for 1 minute
# time.sleep(60)
