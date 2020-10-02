# TweetSentiment Python Package - EC601 -
Project 2 using Tweepy and Google Cloud SDK - NLP. Includes example use case of Trump Sentiment Analysis.

## Overview
This project combines the usage of the tweepy, a python package made to handle the twitter API, and Google Cloud NLP (Natural Language Processing) API. The combination of these two tools allows one to query twitter for tweets and analyze the sentiment of them.  

This is signiicant as it allows companies to gauge the response to their products via social media.

## Tweepy
First, we pass tweepy our twitter account credentials in order to be authenticated and we use tweepy to retrieve live tweets. In order to test this functionality, run the script "tweetAPIexample.py"

## Google Cloud SDK - NLP
Once the json file has been created, we use the Google NLP API in order to parse through our list of tweets, run the sentiment analysis on the text portion of each tweet, and then publish our findings in a sentiment_analysis.txt. This file contains the analysis of each tweet 

In order to test this functionality, first you must download your local Google API service account key and set it as an environment variable prior to running the script. These variables must be set at the beginning of every new session. After setting credentials as an environment variable, run the script "sentiment_analysis.py".

## TrumpCard
An example use case for the combination of these two products is a twitter sentiment analysis of Trump. First, we query twitter for the most recent tweets with the hashtag "#trump". Then, we run our sentiment analysis to get a live sentiment score of trump. We output our NLP analysis of each individual tweet and aggregate it in order to get a general understanding of the recent opinions of trump. 

## Sources


