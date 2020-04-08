import tweepy
import os

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))


# Create API object
api = tweepy.API(auth)
user = api.get_user("")
print(user)