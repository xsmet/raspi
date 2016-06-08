#!/usr/bin/env python

from secrets import *
from twython import Twython, TwythonError
import sys, getopt

def main(argv):
	msg = ''
	file = ''
	try:
		opts, args = getopt.getopt(argv, "hm:f:", ["msg=", "file="])
	except getopt.GetoptError:
		print 'tweet.py -m <message> -f <picture>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'tweet.py -m <message> -f <picture>'
			sys.exit()
		elif opt in ('-m', '--msg'):
			msg = arg
		elif opt in ('-f', '--file'):
			file = arg
	if msg != '':
		global api
		api = Twython(APIKEY, APISECRET, ACCESSTOKEN, ACCESSSECRET)
		if file != '':
			tweet_withpic(msg, file)
		else:
			tweet(msg)

def getuser():
	details = api.show_user(screen_name=TWITTERUSER)
	username = details['name']
	print username
	

def tweet(msg):
	api.update_status(status=msg)
	

def tweet_withpic(msg, file):
	photo = open(file, "rb")
	api.update_status_with_media(media=photo, status=tweet)


if __name__ == "__main__":
	main(sys.argv[1:])
