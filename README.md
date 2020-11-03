# Tweet Sentiment Project 2 AND Project 4 - EC601 - TrumpCard
Project 2 using Tweepy and Google Cloud SDK - NLP. Includes example use case of Trump Sentiment Analysis.
Project 4 using Pytest to conduct Unit Tests
TrumpCard is the culmination of these two packages. It is a product which will allow a user to gauge the general sentiment on Trump's twitter reactions.


## Updates + News
### Pinned Note : 
The Tweepy API cannot handle querying tweets with "#trump" too well, Twitter rejects the call with error 429 : Too many requests. This example has been hardcoded to just query for "#BU" instead.**

### Project 4 Update! Testing has been added using python's popular testing package, Pytest. 
Testing features have been added! In order to run these new additions, take a look at the walkthrough in the Project 4 Overview Section.

## Overview - Project 4
This project demonstrates the testing features and utility that Pytest has to offer. The tests we do can be organized into the following catagories:

#### Standard Query

#### 

#### Error Checking
In addition to the testing modules added, I have also added some initial error checking as there was none implemented initially from Project 2 phase. Some of the error checking includes: 

1. Checking User Input to make sure user is passing correct types of input (i.e checking if num_of_tweets is an int, etc).

2. Sanity Checking query size to make sure API does not pass back any errors

3. 

####

## Overview - Project 2
This project combines the usage of the tweepy, a python package made to handle the twitter API, and Google Cloud NLP (Natural Language Processing) API. The combination of these two tools allows one to query twitter for tweets and analyze the sentiment of them.  

This is signicant as it allows companies to gauge the response to their products via social media. 

In order to run this program, first copy this repository over onto your local machine. 



## Tweepy
First, we pass tweepy our twitter account credentials in order to be authenticated and we use tweepy to retrieve live tweets. In order to test this functionality, run the script "tweetAPIexample.py". We limit the number of tweets used in order to not get the API Error code 429.

As stated in the note at the top, Error 429 is due to too many queries in the last 15 minutes. This is an error that I dealt with many times testing out functionality.

In the given example files, the credentials are set to be empty at the beginning of the file so that other users can test functionality with their own credentials. 

## Google Cloud SDK - NLP
Once the json file has been created, we use the Google NLP API in order to parse through our list of tweets, run the sentiment analysis on the text portion of each tweet, and then publish our findings in a sentiment_analysis.txt. This file contains the analysis of each tweet.

In order to test this functionality, first you must download your local Google API service account key and set it as an environment variable prior to running the script. These variables must be set at the beginning of every new session. After setting credentials as an environment variable, run the script "sentiment_analysis.py".

## TrumpCard
An example use case for the combination of these two products is a twitter sentiment analysis of Trump. First, we query twitter for the most recent tweets with the hashtag "#trump". Then, we run our sentiment analysis to get a live sentiment score of trump. We output our NLP analysis of each individual tweet and aggregate it in order to get a general understanding of the recent opinions of trump. 

<center> Example Output :</center>
<center><img src="./Example Outputs/a.PNG" width="50%" /></center>

## Sources
http://docs.tweepy.org/en/v3.5.0/api.html

https://cloud.google.com/natural-language/docs/sentiment-tutorial

https://cloud.google.com/natural-language/docs/setup


