import requests, json, os, urllib.parse
from requests_oauthlib import *
from dotenv import load_dotenv


class TwitterBot(object):
    def __init__(self):
        load_dotenv()
        apiKey = os.environ.get('apiKey')
        apiSecretKey = os.environ.get('apiSecretKey')
        bearerToken = os.environ.get('bearerToken')
        accessToken = os.environ.get('accessToken')
        accessTokenSecret = os.environ.get('accessTokenSecret')
        self.auth = OAuth1(client_key = apiKey, 
                           client_secret = apiSecretKey, 
                           resource_owner_key = accessToken, 
                           resource_owner_secret=accessTokenSecret)
        self.lookupURL = 'https://api.twitter.com/1.1/statuses/lookup.json?id='
        self.newTweetUrl = 'https://api.twitter.com/1.1/statuses/update.json?status='
        self.tweetStatusUrl = 'https://api.twitter.com/1.1/statuses/show.json?id='
        self.getUserUrl = 'https://api.twitter.com/1.1/users/lookup.json?screen_name='
        self.tweetSearchUrl = 'https://api.twitter.com/1.1/search/tweets.json?q='
        self.deleteTweetUrl = 'https://api.twitter.com/1.1/statuses/destroy/'
    
    def lookup(self, tweetId):
        lookupFormattedUrl = self.lookupUrl + str(tweetId)
        response = requests.get(lookupFormattedUrl, auth = self.auth)
        return response.text
    
    def tweet(self, tweetContents):
        formattedTweet = urllib.parse.quote(tweetContents)
        newTweetFormattedUrl = self.newTweetUrl + formattedTweet
        newTweet = requests.post(newTweetFormattedUrl, auth = self.auth)
        return newTweet.text
    
    def getTweetStatus(self, tweetId):
        tweetStatusFormattedUrl = self.tweetStatusUrl + str(tweetId)
        tweetStatus = requests.get(tweetStatusFormattedUrl, auth = self.auth)
        return tweetStatus.text
    
    
    def getUser(self, username):
        getUserFormattedUrl = self.getUserUrl + username
        getUser = requests.get(getUserFormattedUrl, auth = self.auth)
        return getUser.text
    
    def tweetSearch(self, searchString):
        tweetSearchFormattedUrl = self.tweetSearchUrl + searchString
        tweetSearch = requests.get(tweetSearchFormattedUrl, auth = self.auth)
        return tweetSearch.text
    
    def deleteTweet(self, tweetID):
        deleteTweetFormattedUrl = self.deleteTweetUrl + str(tweetID) + '.json'
        deletedTweet = requests.post(deleteTweetFormattedUrl, auth = self.auth)
        return deletedTweet.txt
    
    def makeTweetUrl(self, tweetId):
        tweetStatus = self.getTweetStatus(tweetId)
        tweetDict = json.loads(tweetStatus)
        username = tweetDict['user']['screen_name']
        resultUrl = f'https://twitter.com/{username}/status/{tweetId}' 
        return resultUrl
    



twitterBot = TwitterBot()
result = twitterBot.tweet("Tweet Content")
print(result)
loadedResult = json.loads(result)
newTweetID = loadedResult['id']
print("\n\n\n\n\n")
print(f'tweetID = {newTweetID}')
print('Tweet url: ' + twitterBot.makeTweetUrl(newTweetID))