from secrets import *
import tweepy
import json
import requests

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)


try:
	response = requests.get("http://quotes.rest/qod.json")
	quote = json.loads(response.text)
	my_day_quote = quote['contents']['quotes'][0]['quote']
	quote_author = quote['contents']['quotes'][0]['author']
	print(my_day_quote + " - " + quote_author)
	
except: 
    print(response.status_code)

api.update_status(my_day_quote + " - " + quote_author)

