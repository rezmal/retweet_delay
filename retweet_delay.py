
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
try:
  import tweepy
except ImportError:
  import pip
  pip.main(['install', 'tweepy'])
finally:
  globals()['tweepy'] = importlib.import_module('tweepy')


import time, sys, urllib

HASH = '#delayediranianapplications'

# you can get the consumer key from apps.twitter.com
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'XXX'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'XXX'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'XXXX'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'XXX'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
counts = 0
while True:
  tt = api.search(HASH,rpp=100,count=100)
  print(len(tt))
  for t in tt:
    text = t.text
    try:
      api.retweet(t.id)
      counts+=1
      print('[%d] Just retweeted this :\n \t %s'%(counts,text))
      time.sleep(300)# this is necessary to avoid twitter's rules
    except:
      pass
  print('sleeping')
  time.sleep(3600)# this is necessary to avoid twitter's rules

