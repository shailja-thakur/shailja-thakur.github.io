
from flask import Flask, jsonify
import tweepy

app = Flask(__name__)

# Set your Twitter API credentials

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


