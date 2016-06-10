#!/usr/bin/env python

import twitter
import subprocess
from secrets import *

def get_reply(msg):
	process = subprocess.Popen(['./get_reply.sh', msg], stdout=subprocess.PIPE)
	out, err = process.communicate()
	return out


auth = twitter.OAuth(
	consumer_key=APIKEY,
	consumer_secret=APISECRET,
	token=ACCESSTOKEN,
	token_secret=ACCESSSECRET
)

twitter_api = twitter.Twitter(auth=auth)
#Test authentication (should return an object)
#print twitter_api

stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')

msgid = ''
for msg in stream.user():
	if 'direct_message' in msg:
		# is there no ID that uniquely identifies this message in the stream? id_str changes continuously...
		newmsgid = msg['direct_message']['created_at'] + msg['direct_message']['text'] + msg['direct_message']['sender_screen_name']
		if msgid != newmsgid:
			msgid = newmsgid
			user = msg['direct_message']['sender_screen_name']
			message = msg['direct_message']['text']
			datum = msg['direct_message']['created_at']
			line = datum + '\t' + user + ':\t' + message + '\n'
			with open('twitterstream_dm_in.txt', 'a') as tf:
				tf.write(line)
			print line
			try:
				twitter_api.direct_messages.new(user=user, text=get_reply(message))
			except twitter.api.TwitterHTTPError as e:
				print("DM failed: %s" % (str(e)))
