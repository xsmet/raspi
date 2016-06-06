import twitter

keys = []
f = open("twitter.conf", "r")
for line in f:
	keys.append( line.rstrip('\n'))
f.close()

auth = twitter.OAuth(
	consumer_key=keys[0],
	consumer_secret=keys[1],
	token=keys[2],
	token_secret=keys[3]
)

stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in stream.user():
	if 'direct_message' in msg:
		print msg['direct_message']['text']
