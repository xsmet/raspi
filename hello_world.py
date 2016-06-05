from twython import Twython, TwythonError

keys = []
username = "null"

f = open("twitter.conf", "r")

for line in f:
	keys.append( line.rstrip('\n'))
f.close()
api = Twython(keys[0], keys[1], keys[2], keys[3])
try:
	details = api.show_user(screen_name='WhiteberryGhent')
	username = details['name']
except TwythonError as e:
	username = "Exception"

print "Username: connected as %s" % username

tweet = 'Hello world!'
try:
	# api.update_status(status=tweet)
	photo = open("pic.png", "rb")
	api.update_status_with_media(media=photo, status=tweet)
except TwythonError as e:
	print "Error!"
