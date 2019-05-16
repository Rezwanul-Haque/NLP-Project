# Importing Libraries
import numpy as np
import json
import pandas as pd
# The above libraries are needed when data fetched from api
import tweepy

from credentials import *

# Calling API
# Authenticate consumer
auth = Authenticate()
auth.set_consumer_token(consumer_key, consumer_secret)

# setting consumer's access token and secret
auth.set_consumer_access_token(access_token, access_token_secret)

# authenticate user
user = auth.authenticate()

api = tweepy.API(user)

# Provide the query you want to pull the data. For example,
# pulling data for the mobile phone ABC
query = "ABC"

# Fetching top 10 tweets
tweets = api.search(query, count=10, lang='en', exclude='retweets', tweet_mode='extended')

