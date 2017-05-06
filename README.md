# EverTweet

### A sentiment analysis tool to track your emotions over time via tweet history.

## What is EverTweet?
The idea of our application stems from research that associates social media content with the mental health of the users. The target audience of our application is thus all Twitter users who might be curious about how the sentiment expressed in their Twitter content has changed over time. Tweet history is converted to sentiment values, which are then displayed to users over a timeline. Users can specify the number of tweets that they would like to take into account.

## EverTweet (Service Oriented Architecture with Servers)

## How to run locally
1. Install required Python Libraries
```python
pip install -r requirements.txt
```

2. In three different windows, run app.py in the orchestrator folder, sentiment_analyzzer.py in the sentiments folder, and tweet_listener.py in the tweets folder.

```
cd application/orchestrator
python app.py
...
```

3. Open given link in local browser
