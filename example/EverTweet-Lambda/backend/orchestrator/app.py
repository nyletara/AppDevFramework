import json
from flask import Flask, request
# from tweet_listener import get_tweets
# from sentiment_analyzer import get_tweet_sentiments

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='EVERTWEET'
)

@app.route('/getTwitterData/<username>', methods=['GET', 'POST'])
def getTwitterData(username):
	tweets = request.post('<ENDPOINT_URL:PORT>', json=username)
	return json.dumps(tweets)

@app.route('/getSentimentList/<username>', methods=['GET', 'POST'])
def get_sentiment_list(username):
    # tweets = get_tweets(username)
    tweets = request.post('<ENDPOINT_URL:PORT>', json=username)
    sentiments = request.post('<ENDPOINT_URL:PORT>', json=json.loads(tweets))
    return json.dumps(sentiments)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
