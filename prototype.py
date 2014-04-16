#!/usr/bin/env python2.7
# tweet.py by Alex Eames http://raspi.tv/?p=5908  
import tweepy
import sys

# Twitter Account Stuff
# You must have a file listed below that contains 4 lines for:
# Twitter Consumer Key
# Twitter Secret
# Twitter Access Token
# Twitter Token Secret
# iBeaconID
twitterConfigFile = '/home/pi/tools/twitter1.conf'
params = [line.strip() for line in open(twitterConfigFile)]

# Consumer keys and access tokens, used for OAuth
if len(params) >= 4:
    consumer_key = params[0]
    consumer_secret = params[1]
    access_token = params[2]
    access_token_secret = params[3]
    i_beacon_id = params[4]

#print consumer_key
#print consumer_secret
#print access_token
#print access_token_secret
print i_beacon_id

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

tweet_text = "This is Burrito Beacon test tweet" 

# conditionally echoing the piped input
for line in sys.stdin:
        print line
	if i_beacon_id in line:
		if len(tweet_text) <= 140:
			print tweet_text 
			#api.update_status(tweet_text)
