import re 
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	'''
	Generic Twitter Class for sentiment analysis.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		# keys and tokens from the Twitter Dev Console
		consumer_key = 'rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs'
		consumer_secret = '3TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOZhJ9'
		access_token = '82XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWqYZ'
		access_token_secret = 'ZBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOy'

		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			# set access token and secret
			self.auth.set_access_token(access_token, access_token_secret)
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		'''
		Utility function to clean tweet text by removing links, special characters
		using simple regex statements.
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		'''
		Utility function to classify sentiment of passed tweet
		using textblob's sentiment method
		'''
		# create TextBlob object of passed tweet text
		analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		if analysis.sentiment.polarity > 0:
			fo=open("bjp_positive.txt","a")
			fo.write(str(analysis))
			fo.close()
		#	with open("positive.txt","a") as file:
		#		file.write(str(analysis))
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			fo=open("bjp_neutral.txt","a")
			fo.write(str(analysis))
			fo.close()
		#	print (analysis)
		#	with open("neutral.txt","a") as file:
		#		file.write(str(analysis))
			return 'neutral'
		else:
			fo=open("bjp_negative.txt","a")
			fo.write(str(analysis))
			fo.close()
		#	print(analysis)
		#	with open("negative.txt","a") as file:
		#		file.open(str(analysis))
			return 'negative'

	def get_tweets(self, query, count = 200):
		'''
		Main function to fetch tweets and parse them.
		'''
		# empty list to store parsed tweets
		tweets = []

		try:
			# call twitter api to fetch tweets
			fetched_tweets = self.api.search(q = query, count = count)

			# parsing tweets one by one
			for tweet in fetched_tweets:
				# empty dictionary to store required params of a tweet
				parsed_tweet = {}

				# saving text of tweet
				parsed_tweet['text'] = tweet.text
				# saving sentiment of tweet
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

				# appending parsed tweet to tweets list
				if tweet.retweet_count > 0:
					# if tweet has retweets, ensure that it is appended only once
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)

			# return parsed tweets
			return tweets

		except tweepy.TweepError as e:
			# print error (if any)
			print("Error : " + str(e))

def main():
	# creating object of TwitterClient Class
	api = TwitterClient()
	# calling function to get tweets
	tweets = api.get_tweets(query = '#BJP', count = 200)

	# picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	
	# percentage of positive tweets
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	pos=(100*len(ptweets)/len(tweets))
	# picking negative tweets from tweets
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	
	# percentage of negative tweets
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	neg=(100*len(ntweets)/len(tweets))
	# percentage of neutral tweets
	jtweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
	print("Neutral tweets percentage: {} %".format(100*len(jtweets)/len(tweets)))
	neu=(100*len(jtweets)/len(tweets))

#writing the results into a file for furthur accessing
	res_file=open("result.txt","w")
	res_file.write((str(pos)) + "\n")
	res_file.write((str(neg)) + "\n")
	res_file.write((str(neu)) + "\n")
	res_file.close()

if __name__ == "__main__":
	# callinig main function
	main()

