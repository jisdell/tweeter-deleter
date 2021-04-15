#Big thanks to Alberta Odamea Anim-Ayeko at https://towardsdatascience.com/python-tweet-deleter-3b1154830f3a for the guide! Really helped me learn how this works!

import tweepy 
import datetime
import json

consumer_key= '#####################'
consumer_secret= '#####################'
access_key= '#####################'
access_secret= '#####################'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
twitter_API = tweepy.API(auth)

cutoff_date = datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(days=2282)
print(cutoff_date)

alltweets = open('Your File Here', 'r', encoding='UTF-8')
tweet_archive = json.load(alltweets)

old_tweet_ids = []
for tweet in tweet_archive:
    d = datetime.datetime.strptime(tweet['tweet']['created_at'], '%a %b %d %H:%M:%S %z %Y')
    if d < cutoff_date:
     old_tweet_ids.append(tweet['tweet']['id_str'])
     #twitter_API.destroy_status(tweet['tweet']['id_str']) #TEST RUN WITH API LINE OFF TO CONFIRM DATES
     print(tweet['tweet']['created_at'] + " " + tweet['tweet'] ['id_str'] + ' deleted successfully')
print(str(len(old_tweet_ids)) + ' old tweets have been deleted…')