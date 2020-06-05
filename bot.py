import time
import tweepy
import KEYS_AND_TOKENS as k

# Authenticate to Twitter
auth = tweepy.OAuthHandler(k.CONSUMER_KEY, k.CONSUMER_SECRET)
auth.set_access_token(k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
while True:
    api.update_status("@realDonaldTrump this is your hourly reminder that you are Orange.")
    time.sleep(3600)