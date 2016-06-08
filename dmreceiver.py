#!/usr/bin/env python

import twitter
from secrets import *

auth = twitter.OAuth(
	consumer_key=APIKEY,
	consumer_secret=APISECRET,
	token=ACCESSTOKEN,
	token_secret=ACCESSSECRET
)

stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in stream.user():
	if 'direct_message' in msg:
		with open('twitterstream_dm_in.txt', 'a') as tf:
			tf.write(msg['direct_message']['text'] + '\n')
