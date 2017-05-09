import json
import requests

def tweet_lambda_handler(event, context):
	username = event['username']
	tweetnum = event['tweetnum']
	user_tweets = get_sentiment_list(username, tweetnum)
	return json.loads(user_tweets)

def get_sentiment_list(username, tweetnum):
	tweets = requests.get('https://20s3rkteqd.execute-api.us-west-2.amazonaws.com/prod/gettweetdata/' + str(username) + '/' + str(tweetnum))	
	sentiments = requests.post('https://ad4idjkc5f.execute-api.us-west-2.amazonaws.com/prod/get-sentiment', json=json.loads(json.loads(tweets.text)))	
	return sentiments.text

# if __name__ == '__main__':
# 	username = 'ishantlguru'
# 	tweets = get_sentiment_list(username)
# 	print tweets