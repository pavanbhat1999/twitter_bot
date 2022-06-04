from lib2to3.pgen2 import token
import tweepy
from get_quotes import get_quotes

# define all variables 
ACCESS_TOKEN = "1478947519212122114-YBrdfURFpsEB4eQ38pZH1PBhvtVSx9";
ACCESS_TOKEN_SECRET = "arLsvLJT7eDafUQO2SUesYGmm5lIDPZ3Cp6g19hiHaxx9";
API_KEY="O8HdUp0JwJ4fkozxwDjiVWaKZ";
API_KEY_SECRET="XExMWueyXcfKxB7KWA2oselq6NV050SHYl96IFNUh0qp9kHT1b";

CONSUMER_KEY = "GYSDpAs24mst1paRiT9PQIcf8";
CONSUMER_SECRET = "7KQuPfh2a7C85TKA0NSMm6dfnLqJ6ewMmurO27zOnSzy1JrlTk";
CLIENT_ID ="UldHcmt4bV9OdUFabWU3c29IY0Y6MTpjaQ";
CLIENT_SECRET="34vaoiCZAs6akJNx2Lb2KnbQ1ReT9pX8I2vdn0AZanvmBVw6co";

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

api.update_status("Hello Tweepy")

def tweet_bot():
    quote = get_quotes()
    print(quote)
    return


tweet_bot();
