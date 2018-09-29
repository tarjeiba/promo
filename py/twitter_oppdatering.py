import tweepy

# bytt ut nøklene under med dine egne
OAUTH_TOKEN = "0y1Fewz5D8r83r06848qGwB850rbf23fdascOZvxP2MVF0p63z9HZU-6z7"
OAUTH_SECRET = "2ae6zeVgY46g9JUKp2LLYobasdfQZsXDVAwQ4JQqhbvAR9hGzp"
CONSUMER_KEY = "DFWhHzNORWWIMjNnjosdfaSKV740Qq"
CONSUMER_SECRET = "pxpC6HUNGuqbsofgMz0VrxPD1BffASDfDGR12a6XAzDfPVNRRQl7Ngpt3J8BM"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

# api = tweepy.API(auth)
# api.update_status('Hei på deg, verden!')

# api.
