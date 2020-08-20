# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:51:52 2020

@author: addyk
"""
"""
Important stuff to always run
"""
pip install requests_oauthlib #run this only if requests_oathlib isn't already installed
import requests
import json
import urllib.parse
from requests_oauthlib import *
from APIauthcodes import * #Private file that contains all auth codes for all apps
twitterauth() #Function that loads in twitter-specific auth codes
from APIauthcodes import * #Needs to be run a second time for some reason for the Twitter codes to actually be loaded into the system - not sure why
#Needs 4 main keys: a client key, client secret key, an access token, and the secret access token. 
#All 4 can be found in the app page in the Twitter Developer Portal.
auth = OAuth1(client_key = APIkey, client_secret = APISecretkey, resource_owner_key = AccessToken, resource_owner_secret=AccessTokenSecret)
#%%
#Lookup Tweet info by Tweet ID
lookup = 'https://api.twitter.com/1.1/statuses/lookup.json?id=1295853588632281090'
response = requests.get(lookup, auth=auth)
print(response.text)
"""
Authentication works, but error message is that id parameter is missing
"""
#%%
#Update tweetcontent object with content of tweet, then run the cell to push the tweet
tweetinput = "Enter contents of tweet here"
tweetcontent = urllib.parse.quote(tweetinput)
newtweeturl = f'https://api.twitter.com/1.1/statuses/update.json?status={tweetcontent}'
newtweet = requests.post(newtweeturl, auth = auth)
print(newtweet.text)
#%%
#Get Status of a tweet
tweetID = '1184595700845367299'
tweetstatusurl = f'https://api.twitter.com/1.1/statuses/show.json?id={tweetID}'
tweetstatus = requests.get(tweetstatusurl, auth = auth)
print(tweetstatus.text)
#%%
#Get Users/Lookup
userID = 'addykan'
getusersurl = f'https://api.twitter.com/1.1/users/lookup.json?screen_name={userID}'
getuser = requests.get(getusersurl, auth = auth)
print(getuser.text)
#%%
#Search tweets
q = '@addykan'
twitsearchurl = f'https://api.twitter.com/1.1/search/tweets.json?q={q}'
getsearch = requests.get(twitsearchurl, auth = auth)
print(getsearch.text)
#%%
#Delete a tweet
destructid = '1295791220673978373'
twitdestructurl = f'https://api.twitter.com/1.1/statuses/destroy/{destructid}.json'
deletetweet = requests.post(twitdestructurl, auth = auth)
print(deletetweet.text)
#%%
#Get timeline with parameters
tweetnum = '3'
username = 'addykan'
timelineurl = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}&count={tweetnum}'
timeline = requests.get(timelineurl, auth = auth)
print(timeline.text)
#%%
#Add all tweet IDs to a list 1x
alltweetID = []
username = 'addykan'
maxid = '1183111562162294789'
include_rts = 'false'
count = '3200'
timelineurl = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}&max_id={maxid}&include_rts={include_rts}&count={count}'
timeline = requests.get(timelineurl, auth = auth)
alltweets = json.loads(timeline.text)
for i in range(len(alltweets)):
    alltweetID.append(alltweets[i]['id_str'])
print(alltweetID)
print(len(alltweetID))
#%%
#Continously execute previous function to get all tweets at once
username = 'addykan'
include_rts = 'false'
count = '200'
while True:
    maxid = alltweets[-1]['id_str']
    timelineurl = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}&max_id={maxid}&include_rts={include_rts}&count={count}'
    timeline = requests.get(timelineurl, auth = auth)
    alltweets = json.loads(timeline.text)
    for i in range(len(alltweets)):
        alltweetID.append(alltweets[i]['id_str'])
    print(alltweetID)
    print(len(alltweetID))
#%%
#delete tweets en masse
for i in alltweetID:
    destructid = str(i)
    twitdestructurl = f'https://api.twitter.com/1.1/statuses/destroy/{destructid}.json'
    deletetweet = requests.post(twitdestructurl, auth = auth)
print(deletetweet.text)
#%%
#Collecting a list of all RT'd tweets
#First, add all RT IDs to a list 1x
RTID = []
username = 'addykan'
maxid = '1295853750364643336'
include_rts = 'true'
count = '200'
RTsurl = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}&max_id={maxid}&include_rts={include_rts}&count={count}'
RTS = requests.get(RTsurl, auth = auth)
allRTs = json.loads(RTS.text)
for i in range(len(allRTs)):
    RTID.append(allRTs[i]['id_str'])
print(RTID)
print(len(RTID))
#%%
#Continously extend RTID to include all RT'd tweets
username = 'addykan'
include_rts = 'true'
count = '200'
while True:
    maxid = allRTs[-1]['id_str']
    RTsurl = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}&max_id={maxid}&include_rts={include_rts}&count={count}'
    RTS = requests.get(RTsurl, auth = auth)
    allRTs = json.loads(RTS.text)
    for i in range(len(allRTs)):
        RTID.append(allRTs[i]['id_str'])
    print(RTID)
    print(len(RTID))
#%%
#Unretweet a single tweet, using tweet ID
tweetID = '1296130224736747520'
unRTurl = f'https://api.twitter.com/1.1/statuses/unretweet/{tweetID}.json'
unRT = requests.post(unRTurl, auth = auth)
print(unRT.text)
#%%
#Unretweet multiple tweets, iteratively using a premade list
for i in RTID:
    unRTid = str(i)
    unRTurl = f'https://api.twitter.com/1.1/statuses/unretweet/{unRTid}.json'
    unRT = requests.post(unRTurl, auth = auth)
print(unRT.text)
#%%
#Get a list of up to 200 liked tweets, depending on count
count = '200'
likesurl = f'https://api.twitter.com/1.1/favorites/list.json?count={count}'
likesID = []
likes = requests.get(likesurl, auth = auth)
likespy = json.loads(likes.text)
for i in range(len(likespy)):
    likesID.append(likespy[i]['id_str'])
print(likesID)
print(len(likesID))
#%%
#Extension of likesID list to include all tweets (or until Twitter breaks)
while True:
    max_id = likesID[-1]
    likesurl= f'https://api.twitter.com/1.1/favorites/list.json?count=200&max_id={max_id}'
    likes = requests.get(likesurl, auth = auth)
    likespy = json.loads(likes.text)
    for i in range(len(likespy)):
        likesID.append(likespy[i]['id_str'])
    print(likesID)
    print(len(likesID))
#%%
#Unlike all tweets in a premade list
for i in likesID:
    unlikeID = i
    unlikeurl = f'https://api.twitter.com/1.1/favorites/destroy.json?id={unlikeID}'
    unlike = requests.post(unlikeurl, auth = auth)
print('done)')
print(unlike.text)
print('extra done')