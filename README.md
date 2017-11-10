# Emotion-detector-election-win-or-loss

Detecting the emotion using twitter through NLP techinques i.e Sentimental analysis and Machine Learning Bayesian Model.

##Synopsis 
Twitter a social website where people comment on several on going topics called tweets. If the tweets related to a particular topic a overall sentimental analysis can be drawn out, which would bring out the emotion of people of those who tweet. This can used to analyse sevaral conclusion.The Election analysis uses the same to drive out the emotion of people.

## Prerequisation 
1. Python 2.7
2. Twitter Account
3. Regular Expression library
4. tweepy library
5. textblob library

## Creating an Twitter Api
To create a Api click here [Twitter_Api](https://apps.twitter.com/)

## Main file
Running this python file will automatically run all the respective python files for each parties.
Each party files would individually access the tweeter account through the tweeter api for extracting tweets.

## Data Generation files
All the files have the same functioning except the query that is made, the counts are also mentioned here i.e the number of tweets that need to be considered.
Initially the main function is called which would, in turn, call the Twitter client finction. 3.Here the credentials are taken and a connection to the api is made.
The control is returned to the main function which would next call the next function which would retrive the tweets now.
The matching tweets are put in an array and then passed into another function to get it cleaned. 6 Using textblob library the tweets are cleaned and then checked for its sentiment.
For cross checking we have put the positive, negative and neutral sentiment into different files geiint a count simultaneously.
Using these counts the individual percentage can be calculated.
This is then graphically visualized.
The overall graph is shown below.

![Alt text](a.png?raw = true "Results")

