import tweepy
import sys
import json #To write file as json format

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def Authorization_Setup():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api

#Write tweets information to file as json format.
def Write_tweets_to_File(Input_list,target_filename):
    data = []
    filename = "%s.json" % target_filename
    Tweets_text = open(filename, 'w') 
    for status in Input_list:
        data.append(status._json)
    json.dump(data,Tweets_text)
    Tweets_text.close

#Search tweets based on Hashtag and time.
def QueryTweets(API,Hashtag,Count_Number,since_id):
    Hashtag_Tweets = tweepy.Cursor(API.search,q=Hashtag,count=Count_Number,since=since_id)
    Write_tweets_to_File(Hashtag_Tweets.items(),'Hashtag_Tweets')

if __name__ == "__main__":
    API = Authorization_Setup()
    API.wait_on_rate_limit=True
    # the hashtag has been switched to '#BU' in order to avoid twitter API error 429 
    QueryTweets(API,"#Boston University",5,"2020-9-28")
