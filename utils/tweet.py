import os
import tweepy
from dotenv import load_dotenv

from utils.date import now

load_dotenv()

file = os.getcwd() + '/reddit.png'

# TWITTER API CREDENTIALS
consumerKey = os.environ.get("CONSUMER_KEY")
consumerSecret = os.environ.get("CONSUMER_SECRET")
accessToken = os.environ.get("ACCESS_TOKEN")
accessTokenSecret = os.environ.get("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuth1UserHandler(
    consumerKey,
    consumerSecret,
    accessToken,
    accessTokenSecret
)
client = tweepy.API(auth)

# The app and the corresponding credentials must have the Write permission


def tweet(message):
    media_file = client.media_upload(filename=file)
    response = client.update_status(status=message, media_ids=[media_file.media_id_string])
           
    print(response)                               
    print(
        'Done Tweeting...............................', now()
    )

