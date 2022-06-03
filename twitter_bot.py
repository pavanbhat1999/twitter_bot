from lib2to3.pgen2 import token
import tweepy
from get_quotes import get_quotes


def tweet_bot():
    quote = get_quotes()
    print(quote)
    return


tweet_bot();











# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("Ln9iLKOYbGlAODjByLLjcOBpe",
#     "HJt5EDJDFSZG9D1Iu1njMaYL8QN0jsn1QfEYRnUQFUovU9TPnr")
# auth.set_access_token("1478947519212122114-44kO8zx980E6kCfANBco3XuEoDwUe4", 
#     "iQFap825Z5pAnGdHQDgMGRcbuwae9HoCaS4iD1u8t9k0p")

# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")



  

#     # access token
#     # 1478947519212122114-44kO8zx980E6kCfANBco3XuEoDwUe4
#     # access token secret 
#     # iQFap825Z5pAnGdHQDgMGRcbuwae9HoCaS4iD1u8t9k0p

#     # bearer token 
#     # AAAAAAAAAAAAAAAAAAAAAFIvdQEAAAAA%2Fb2c5dcFzI0Df3yKHCmtEF09Zj0%3D2nH38geD0yY2QadJWO4hjpli5dVEbuOAw7ZEebjeOQSTDH2vkw
