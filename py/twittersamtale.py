import time
import tweepy
import json

secrets_filename = 'oppdatering.secrets'

# oppdatering.secrets er ganske enkelt en fil som inneholder kodene twitter tildelte oss
# da vi registrerte boten vår. Innholdet i fila ser ut som noe à la dette (inkludert krøllparenteser:
# {
#      "OAUTH_TOKEN" : "0y1Fewz5D8r83r06848qGwB850rbf23fdascOZvxP2MVF0p63z9HZU-6z7",
#     "OAUTH_SECRET" : "2ae6zeVgY46g9JUKp2LLYobasdfQZsXDVAwQ4JQqhbvAR9hGzp",
#     "CONSUMER_KEY" : "DFWhHzNORWWIMjNnjosdfaSKV740Qq",
#     "CONSUMER_SECRET" : "pxpC6HUNGuqbsofgMz0VrxPD1BffASDfDGR12a6XAzDfPVNRRQl7Ngpt3J8BM"
# }
# Merk: Dette er sjølsagt ikke de faktiske kodene. De bør jeg, og du, holde hemmelig

api_keys = {}
with open(secrets_filename, 'r') as f:
    api_keys = json.loads(f.read())

auth = tweepy.OAuthHandler(api_keys['CONSUMER_KEY'], api_keys['CONSUMER_SECRET'])
auth.set_access_token(api_keys['OAUTH_TOKEN'], api_keys['OAUTH_SECRET'])

api = tweepy.API(auth)

min_id = 1072837266496765952

if partall:
    print("Oppdaterer tidslinje.")
    tidslinje = api.home_timeline()
    for tweet in tidslinje:
        if tweet.in_reply_to_status_id == min_id:
            print("Funnet svar.")
            svar_til_id = tweet.id
            bruker = tweet.author.screen_name
            print(tweet.text)
            tekst = input("Hva vil du si til dette? >>> ")
            mitt_svar = api.update_status(f"@{bruker} " + tekst,
                                          in_reply_to_status_id=svar_til_id)
            min_id = mitt_svar.id
    time.sleep(61)


print("Svar sendt. Gå hjem.")
