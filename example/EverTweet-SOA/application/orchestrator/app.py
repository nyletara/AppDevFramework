import json
from flask import Flask, request, render_template
import requests
# from tweet_listener import get_tweets
# from sentiment_analyzer import get_tweet_sentiments

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='EVERTWEET'
)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/getTwitterData/<username>', methods=['GET', 'POST'])
def getTwitterData(username):
	tweets = request.post('<ENDPOINT_URL:PORT>', json=username)
	return json.dumps(tweets)

@app.route('/getSentimentList/<username>/<numTweets>', methods=['GET', 'POST'])
def get_sentiment_list(username, numTweets):
    tweets = requests.get('http://0.0.0.0:6050/getTwitterData/' + username + '/' + numTweets)
    sentiments = requests.post('http://0.0.0.0:5050/getTweetSentiments', json=tweets.content.decode('utf-8'))
    return sentiments.content

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
