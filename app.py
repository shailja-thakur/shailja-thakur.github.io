
from flask import Flask, jsonify
import tweepy

app = Flask(__name__)

# Set your Twitter API credentials
consumer_key = 'WDuIdMfpfW4x3VYl0Z9PjUIXy'
consumer_secret = 'da0jRyadIreruC8EJl7WlbVZl6Oi512FVvoEVCCAY9QzGtfK9u'
access_token = '1534450153-e5kqD6i9GCKUZVH9TI894dMmyXOLAWJ1MebH34b'
access_token_secret = 'OEB2R6GIqXJn9vw4TWIdJPemIzjMnlvEp5GDU43ZDQgT0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

@app.route('/tweets')
def get_tweets():
    try:
        # Fetch your mentions and tweets
        mentions = api.mentions_timeline(count=10)  # Fetch 10 mentions
        user_tweets = api.user_timeline(screen_name='shailjaThakur3', count=10)  # Fetch 10 of your tweets
        
        # Combine mentions and your tweets
        tweets = []
        for tweet in mentions + user_tweets:
            tweets.append({
                'text': tweet.text,
                'user': tweet.user.screen_name,
                'created_at': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        
        return jsonify({'tweets': tweets})
    except tweepy.TweepError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()


