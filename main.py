import tweepy
import time
import datetime
import json
import requests
import random

def getCatFact():
    temp = requests.get('https://cat-fact.herokuapp.com/facts')
    temp2 = temp.json()
    num = random.randrange(260)
    temp3 = temp2['all'][num]['text']
    print(temp3)
    return temp3


print("Twitter Bot activated")



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)

#for tweet in tweepy.Cursor(api.user_timeline,id='meowmeowmeozies').items():
#    if 'hi ' in tweet.text.lower():
#        api.update_status('@' + tweet.user.screen_name + ' hi!', in_reply_to_status_id = tweet.id)
#        print('responded with hi!')

for a in range(0,100):
    factid = getCatFact()
    api.update_status('Did you know ? ' + factid + ' Wow !')
    currenttime = datetime.datetime.now()
    print('Meow at ' + str(currenttime) + '!')
    time.sleep(60)
